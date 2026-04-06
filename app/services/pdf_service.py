import pdfplumber
import io
from fastapi import UploadFile, HTTPException


async def extract_text_from_pdf(file: UploadFile) -> str:
    """
    Accepts an uploaded PDF file and extracts all text from it.
    Returns the raw text as a string.
    """

    # Step 1: Check it's actually a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    # Step 2: Read the file contents into memory
    contents = await file.read()

    # Step 3: Extract text page by page
    try:
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # Step 4: Make sure we actually got some text
        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text. The PDF may be scanned or image-based."
            )

        return text.strip()

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process PDF: {str(e)}"
        )