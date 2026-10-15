from pydantic import BaseModel


class UploadAccepted(BaseModel):
    document_id: str
    status: str
