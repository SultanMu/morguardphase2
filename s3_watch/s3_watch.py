import time
import logging
import s3_access as s3
from db_handler import CompanyDatabaseHandler
import aiohttp
import argparse
import asyncio
import datetime
from dateutil.relativedelta import relativedelta
import re
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
from os import getenv



class S3BucketPoller:
    def __init__(self, bucket_name, polling_interval=3):
        self.bucket_name = bucket_name
        self.polling_interval = polling_interval
        self.last_seen_files = {}
        self.db_conn = CompanyDatabaseHandler(host=getenv('host'),database=getenv('name'),user=getenv('user'),password=getenv('password'),port=getenv('port'))
    async def index_file(self, url: str, file_name: str, folder_name: str, max_retries: int = 5, retry_interval: int = 10):
        attempt = 0
        while attempt < max_retries:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post("http://mguard-file-processor-phase-2:8800/process/", data={"content": url}) as response:
                        response.raise_for_status()  
                        texts = await response.json()
                        text_data = texts.get("fields", [])

                    if text_data:
                        pattern =  r'\b\w+\d\w* -| - [A-Za-z]+ \d{1,2}, \d{4}|\.pdf|\.docx'
                        date_pattern = r"(\bJan|\bFeb|\bMar|\bApr|\bMay|\bJun|\bJul|\bAug|\bSep|\bOct|\bNov|\bDec) (\d{1,2}) (\d{4})"
                        if text_data.get("Date Created") == "Not Available":
                            date_match = re.search(date_pattern,file_name)
                            if date_match:
                                month = date_match.group(1)
                                day = date_match.group(2)
                                year = date_match.group(3)
                                date_obj = datetime.strptime(f"{day} {month} {year}", "%d %b %Y")
                                formatted_date = date_obj.strftime("%d-%m-%Y")
                                text_data["Date Created"] = formatted_date
                                if text_data.get("Next Assessment Date") == "Not Available":
                                    next_data = date_obj + relativedelta(months=3)
                                    next_asses_date = next_data.strftime("%d-%m-%Y")
                                    text_data["Next Assessment Date"] = next_asses_date
                            else:
                                text_data["Date Created"] = "Not Available"
                        if text_data.get("Company") == "Not Available":
                            text_data["Company"] = re.sub(pattern, '', file_name)
                        
                        if text_data.get("Report Title") == "Not Available":
                            text_data["Report Title"] = re.sub(pattern, '', file_name)

                        
                        return {file_name:text_data}
                    else:
                        return {"exception": "Failed to process", "file_name": file_name}


            except aiohttp.ClientError as e:
                attempt += 1
                logger.info(f"Attempt {attempt} failed: {e}. Retrying in {retry_interval} seconds...")

                if attempt < max_retries:
                    await asyncio.sleep(retry_interval)  # Wait before retrying
                else:
                    return {"exception": "Max retries reached", "file_name": file_name}

            

    def list_files(self):
        """List files in the S3 bucket and return a dictionary with file names and their last modified timestamps."""
        try:
            file_folder = {}
            files_data = {}
            folders = s3.list_folders_in_bucket(self.bucket_name)
            for folder in folders:
                files,dates_mod = s3.expand_s3_folder(self.bucket_name,folder)
                file_folder.update({file: folder for file in files})
                files_data.update({file:date_mod for file,date_mod in zip(files,dates_mod)})
            return files_data,file_folder
        except Exception as e:
            logger.error(f"Error listing files in bucket {self.bucket_name}: {e}")
            return {},{}

    def detect_changes(self, current_files):
        """Detect new or modified files by comparing current state with the last seen state."""
        new_files = []
        modified_files = []

        for file_name, last_modified in current_files.items():
            if file_name not in self.last_seen_files:
                new_files.append(file_name)
            elif self.last_seen_files[file_name] != last_modified:
                modified_files.append(file_name)

        return new_files, modified_files

    async def process_new_files(self, new_files,folder_map):
        """Handle newly uploaded files."""
        if new_files:
            logger.info(f"New files detected: {new_files}")
            await self.call_index_function(new_files,folder_map)

    async def process_modified_files(self, modified_files,folder_map):
        """Handle modified files."""
        if modified_files:
            logger.info(f"Modified files detected: {modified_files}")
            await self.call_index_function(modified_files,folder_map)

    async def call_index_function(self, files,folder_map:dict):
        """Call the index_file function for each new or modified file."""
        file_info_data = []
        for file_name in files:
            folder_name = folder_map.get(file_name)
            file_url = s3.get_s3_file_url(self.bucket_name,folder_name,file_name)
            result = await self.index_file(file_url, file_name, folder_name)
            if result.get("exception",None):
                logger.info(f"{str(result)}")

            else:
                file_info_data.append(result)

        files_data = [
            {
                'type': file_info_dict.get('Report Type'),  # No quotes around the key name
                'title': file_info_dict.get('Report Title', "0"),
                'created_date': file_info_dict.get('Date Created'),
                'next_asses_date': file_info_dict.get('Next Assessment Date', "NA"),
                'company': file_info_dict.get('Company', "NA"),
                'author': file_info_dict.get('Author', "NA"),
                'summary': file_info_dict.get('Summary'),
                'file_name': file_name,
                'flag': True if "Not Available" in file_info_dict.values() else False
            }
            for file_data in file_info_data for file_name, file_info_dict in file_data.items()
        ]
        logger.info("Inserting data...")
        self.db_conn.insert_data(files_data=files_data)
        logger.info("Files inserted "+"{}".format(files))
    async def poll(self):
        """Poll the S3 bucket for changes in a loop."""
        logger.info(f"Starting to poll S3 bucket {self.bucket_name} every {self.polling_interval} hours.")
        while True:
            current_files,folder_map = self.list_files()
            new_files, modified_files = self.detect_changes(current_files)

            if new_files:
                await self.process_new_files(new_files,folder_map)
            if modified_files:
                await self.process_modified_files(modified_files,folder_map)

            self.last_seen_files = current_files

            time.sleep(self.polling_interval*60*60)

S3_BUCKET_NAME = getenv("BUCKET_NAME")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="S3 Bucket Poller")
    parser.add_argument(
        "-i", "--interval", type=int, default=3, help="Polling interval in hours"
    )
    args = parser.parse_args()
    s3_poller = S3BucketPoller(S3_BUCKET_NAME, polling_interval=args.interval)
    asyncio.run(s3_poller.poll())