from fastapi import FastAPI, UploadFile, File, HTTPException
from app.pdf_utils import extract_text_from_pdf
from app.ai_utils import generate_summary
import os
import uuid

from pydantic import BaseModel

class ExtractTextRequest(BaseModel):
    saved_filename: str
class SummaryRequest(BaseModel):
    saved_filename: str

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {
        "message": "Welcome to Cognify AI"
    }

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    unique_id = str(uuid.uuid4())

    saved_filename = f"{unique_id}_{file.filename}"

    file_path = os.path.join(
    UPLOAD_FOLDER,
    saved_filename
)   

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
    "filename": file.filename,
    "saved_filename": saved_filename,
    "message": "PDF uploaded successfully"
}
@app.post("/extract-text")
async def extract_text(request: ExtractTextRequest):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        request.saved_filename
    )

    text = extract_text_from_pdf(file_path)

    return {
        "saved_filename": request.saved_filename,
        "text": text
    }
@app.post("/summarize")
async def summarize(request: SummaryRequest):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        request.saved_filename
    )

    text = extract_text_from_pdf(file_path)

    summary = generate_summary(text)

    return {
        "saved_filename": request.saved_filename,
        "summary": summary
    }