from fastapi import APIRouter, File, UploadFile

from src.api.errors import (
    DuplicateDocumentError,
    FileTooLargeError,
    InvalidFormatError,
    PDFValidationError,
)
from src.api.schemas import PDFUploadResponse

router = APIRouter(prefix="/pdf", tags=["PDF"])

MAX_SIZE_MB = 10
ALLOWED_TYPES = {"application/pdf"}


@router.post("/extract", response_model=PDFUploadResponse)
async def extract_pdf(
    file: UploadFile = File(...),
) -> PDFUploadResponse:
    if file.size and file.size > MAX_SIZE_MB * 1024 * 1024:
        raise FileTooLargeError(MAX_SIZE_MB)

    if file.content_type not in ALLOWED_TYPES:
        raise InvalidFormatError()

    content = await file.read()

    if len(content) > MAX_SIZE_MB * 1024 * 1024:
        raise FileTooLargeError(MAX_SIZE_MB)

    return PDFUploadResponse(
        file_id="test123",
        filename=file.filename or "document.pdf",
        checksum="abc123",
        text_preview="Sample text...",
        is_duplicate=False,
    )