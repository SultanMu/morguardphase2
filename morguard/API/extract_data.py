import aiohttp   
import re     
class ExtractData:    
    async def index_file(self,url:str,file_name:str,folder_name:str):
        async with aiohttp.ClientSession() as session:            
            async with session.post("http://mguard-file-processor-phase-2:8000/process/",data={"content":url}) as response:
                response.raise_for_status()
                texts= await response.json()
                text_data = texts.get("fields",[])
            if len(text_data) == 0:
                return {"exception":"Failed to process","file_name":file_name}
            
            text_data["Report Type"] = folder_name
            pattern =  r'\b\w+\d\w* -| - [A-Za-z]+ \d{1,2}, \d{4}|\.pdf|\.docx'
            
            if text_data.get("Company") == "Not Available":
                text_data["Company"] = re.sub(pattern, '', file_name)
            
            if text_data.get("Report Title") == "Not Available":
                text_data["Report Title"] = re.sub(pattern, '', file_name)

            
            return {file_name:text_data}