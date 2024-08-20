import pdfplumber
from io import BytesIO
import re
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/process/")
async def process_pdf(request:Request):
    texts = []
    stream = await request.body()
    try:
        with pdfplumber.open(BytesIO(stream)) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = re.sub(r"\s+", " ", page.extract_text().strip())
                if text:
                    texts.append(text)
            texts.append("Report Metadata :" + str(pdf.metadata))
        return {"texts": texts}
    except Exception as e:
        return {"exception":str(e)}

    