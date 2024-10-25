from io import BytesIO
import json
import aiohttp
import urllib.parse
from fastapi import FastAPI, Request
from llama_parser import FileParser
from parsing_instructions import parsing_instructions,query
from fastapi.responses import JSONResponse
app = FastAPI()


@app.post("/process/")
async def process_pdf(request:Request):
    try:
        url = await request.body()
        url = urllib.parse.unquote(url.decode()[8:])
        async with aiohttp.ClientSession() as session: 
            async with session.get(url) as response:
                    response.raise_for_status()
                    content = await response.read()
        response = FileParser().retrieve(parsing_instructions=parsing_instructions,query=query,file=BytesIO(content),url=url)
        return {"fields":json.loads(str(response))}
    except Exception as e:
        print(e)
        return {"exception":str(e)}

@app.get("/health")
async def health_check():
    return JSONResponse(status_code=200, content={"status": "ok"})
    

    