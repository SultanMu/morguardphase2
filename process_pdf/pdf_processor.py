import pdfplumber
from io import BytesIO
import re
import aiohttp
import urllib.parse
import docx
from fastapi import FastAPI, Request

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
        with pdfplumber.open(BytesIO(content)) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = re.sub(r"\s+", " ", page.extract_text().strip())
                if text:
                    texts.append(text)
            texts.append("Report Metadata :" + str(pdf.metadata))
        return {"texts": texts}
    except Exception as e:
        try:
            doc = docx.Document(BytesIO(content))
            texts = []
            for paragraph in doc.paragraphs:
                text = paragraph.text.strip()
                if text:
                    texts.append(text)
            

            metadata = {
                "title": doc.core_properties.title,
                "author": doc.core_properties.author,
                "created": doc.core_properties.created,
            }            
            texts.append("Report Metadata: " + str(metadata))
            return {"texts": texts}
        
        except Exception as e:
            return {"exception": str(e)}

    