import aiohttp        
class ExtractData:    
    async def index_file(self,url:str,file_name:str,folder_name:str):
        async with aiohttp.ClientSession() as session:            
            async with session.post("http://mguard-file-processor-phase-2:8000/process/",data={"content":url}) as response:
                response.raise_for_status()
                texts= await response.json()
                text_data = texts.get("fields",[])
            if len(text_data) == 0:
                return {"exception":"Failed to process","file_name":file_name}
            else:
                return {file_name:text_data}