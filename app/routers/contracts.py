from fastapi import APIRouter, UploadFile, File
from app.services.pdf_service import extract_text_from_pdf


router = APIRouter(prefix="/contracts", tags=["Contracts"])


@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    """
    Accepts a PDF file upload and returns the extracted text.
    """

    # Call our pdf_service to extract the text
    raw_text = await extract_text_from_pdf(file)

    # Return a simple response for now
    return {
        "filename": file.filename,
        "characters": len(raw_text),
        "preview": raw_text[:500]  # First 500 chars only
    }