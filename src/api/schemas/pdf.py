from pydantic import BaseModel, Field


class PDFUploadRequest(BaseModel):
    filename: str = Field(..., max_length=255)


class PDFUploadResponse(BaseModel):
    file_id: str
    filename: str
    checksum: str
    text_preview: str = Field(..., max_length=500)
    is_duplicate: bool = False


class ErrorResponse(BaseModel):
    error: str
    detail: str | None = None