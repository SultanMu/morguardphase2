from io import BytesIO
import json
import aiohttp
import urllib.parse
from fastapi import FastAPI, Request
from llama_parser import FileParser
from parsing_instructions import parsing_instructions,query
app = FastAPI()


@app.post("/process/")
async def process_pdf(request:Request):
    texts = []
    url = await request.body()
    url = urllib.parse.unquote(url.decode()[8:])
    try:
        async with aiohttp.ClientSession() as session: 
            async with session.get(url) as response:
                    response.raise_for_status()
                    content = await response.read()
        response = FileParser().retrieve(parsing_instructions=parsing_instructions,query=query,file=BytesIO(content))
        return {"fields":json.loads(str(response))}
    except Exception as e:
        print(e)
        return {"exception":e}

    


# @app.post("/process/")
# async def process_pdf(request:Request):
#     texts = []
#     url = await request.body()
#     url = urllib.parse.unquote(url.decode()[8:])
#     try:
#         async with aiohttp.ClientSession() as session: 
#             async with session.get(url) as response:
#                     response.raise_for_status()
#                     content = await response.read()
#         with pdfplumber.open(BytesIO(content)) as pdf:
#             for page_num, page in enumerate(pdf.pages):
#                 text = re.sub(r"\s+", " ", page.extract_text().strip())
#                 if text:
#                     texts.append(text)
#             texts.append("Report Metadata :" + str(pdf.metadata))
#         return {"texts": texts}
#     except Exception as e:
#         try:
#             doc = docx.Document(BytesIO(content))
#             texts = []
#             for paragraph in doc.paragraphs:
#                 text = paragraph.text.strip()
#                 if text:
#                     texts.append(text)
            

#             metadata = {
#                 "title": doc.core_properties.title,
#                 "author": doc.core_properties.author,
#                 "created": doc.core_properties.created,
#             }            
#             texts.append("Report Metadata: " + str(metadata))
#             return {"texts": texts}
        
#         except Exception as e:
#             return {"exception": str(e)}

    