import aiohttp   
import re     
import datetime
from dateutil.relativedelta import relativedelta
class ExtractData:    
    async def index_file(self,url:str,file_name:str,folder_name:str):
        async with aiohttp.ClientSession() as session:            
            async with session.post("http://mguard-file-processor-phase-2:8000/process/",data={"content":url}) as response:
                response.raise_for_status()
                texts= await response.json()
                text_data = texts.get("fields",[])
            if len(text_data) == 0:
                return {"exception":"Failed to process","file_name":file_name}
            
            # text_data["Report Type"] = folder_name
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