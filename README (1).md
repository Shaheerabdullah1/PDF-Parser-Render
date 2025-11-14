# PDF Text Extraction API

This is a simple FastAPI service that extracts text from uploaded PDF files using **pdfplumber**.

## 🚀 Features
- Upload any PDF file
- Extracts text from all pages
- Returns extracted text as JSON
- Lightweight and easy to deploy

---

## 📌 Requirements

Install dependencies:

```bash
pip install fastapi uvicorn pdfplumber python-multipart
```

---

## 📂 Project Structure

```
.
├── main.py
└── README.md
```

---

## 🧠 How It Works

1. A PDF file is uploaded to the `/extract-text` endpoint.
2. The API reads the file bytes.
3. `pdfplumber` opens the PDF and extracts text from each page.
4. All text is combined and returned in a JSON response.

---

## 📝 API Endpoint

### **POST** `/extract-text`

**Body:**  
`file`: PDF uploaded as `multipart/form-data`

**Response:**
```json
{
  "extracted_text": "Full extracted text from PDF..."
}
```

---

## 🧪 Example cURL

```bash
curl -X POST "http://localhost:8000/extract-text"   -F "file=@document.pdf"
```

---

## ▶️ Running the Server

Start FastAPI with Uvicorn:

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🛠 Sample Code (`main.py`)

```python
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
```

---

## 📄 License
This project is open-source and free to use.
