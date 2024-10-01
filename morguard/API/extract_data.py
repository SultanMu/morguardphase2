import aiohttp
from .authorization import Credentials

import os   
# from llama_index.core import VectorStoreIndex,Document
from llama_index.legacy import Document
import json
import re
from . import agents

        
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
                return text_data