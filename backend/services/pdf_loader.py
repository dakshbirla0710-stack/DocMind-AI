import fitz
import shutil
from fastapi import UploadFile
import os
def extract_text_from_pdf(file: UploadFile):
    os.makedirs("uploads", exist_ok=True)
    
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text