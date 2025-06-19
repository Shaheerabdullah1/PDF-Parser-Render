from fastapi import FastAPI, UploadFile, File
import pdfplumber
import io

app = FastAPI()

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    text_output = ""
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_output += page_text + "\n"
    return {"extracted_text": text_output}
