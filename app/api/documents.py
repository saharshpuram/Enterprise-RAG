from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.documents import UploadAccepted
from app.services.ingestion import save_upload

router = APIRouter()


@router.post("/upload", response_model=UploadAccepted, status_code=status.HTTP_202_ACCEPTED)
async def upload_document(file: UploadFile = File(...)) -> UploadAccepted:
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    document_id = str(uuid4())
    await save_upload(file, document_id)
    return UploadAccepted(document_id=document_id, status="uploaded")
