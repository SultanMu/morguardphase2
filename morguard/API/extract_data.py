from io import BytesIO
import pdfplumber
import aiohttp
from .authorization import Credentials
from llama_index.llms.openai import OpenAI
import os   
from llama_index.core import VectorStoreIndex,Document
import json
import re
from . import agents
from llama_index.legacy.vector_stores.postgres import PGVectorStore
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
tenant_id = os.getenv("tenant_id")
class ExtractData:
    def __init__(self):
        self.llm =  OpenAI(temperature=0, model="gpt-4")
    async def create_index(self, documents, show_progress):
        vector_store = PGVectorStore.from_params(
            database=os.getenv("name"),
            host=os.getenv("host"),
            password=os.getenv("password"),
            port=os.getenv("port"),
            user=os.getenv("user"),
            table_name="MguardFileEmbeddings",
            embed_dim=1536,  # openai embedding dimension
        )
        index = VectorStoreIndex.from_documents(documents,show_progress=show_progress,run_async=True)
        # index = KeywordTableIndex.from_documents(documents, llm=self.llm)
        # index.storage_context.add_vector_store(vector_store,)
        return index
        
    
    async def index_file(self,url:str,file_name:str,folder_name:str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()
            async with session.post("http://mguard-file-processor:8000/process/",data={"content":content}) as response:
                response.raise_for_status()
                texts= await response.json()
                text_data = texts.get("texts",[])
            if len(text_data) == 0:
                return {"exception":"Failed to process","file_name":file_name}
        try:
            queries = await agents.get_query(folder_name)
            documents = [Document(text=text) for text in text_data]
            index = await self.create_index(documents,False)
            del documents
            query_engine = index.as_query_engine(llm=self.llm)
            response1 = query_engine.query(queries[0])
            response2 = query_engine.query(queries[1])
            response3 = query_engine.query(queries[2])
            response4 = query_engine.query(queries[3])
            response5 = query_engine.query(queries[4])
            response6 = query_engine.query(queries[5])
            response7 = query_engine.query(queries[6])
            responses = [response1,response2,response3,response4,response5,response6,response7]
            output = {}
            
            for resp in responses:
                output.update(json.loads(str(resp)))
            return {file_name:output}
            # return {"resp":{"data":responses}}
                
        except Exception as e:
            print(str(resp))
            return {"exception":str(e)}