from fastapi import APIRouter, File, UploadFile

from src.api.errors import FileTooLargeError, InvalidFormatError
from src.api.schemas import PDFUploadResponse
from src.core.use_cases.extract_text import ExtractTextUseCase
from src.infrastructure.pdf_client.client import PDFClient

router = APIRouter(prefix="/pdf", tags=["PDF"])

MAX_SIZE_MB = 10
ALLOWED_TYPES = {"application/pdf"}


@router.post("/extract", response_model=PDFUploadResponse)
async def extract_pdf(file: UploadFile = File(...)) -> PDFUploadResponse:
    if file.size and file.size > MAX_SIZE_MB * 1024 * 1024:
        raise FileTooLargeError(MAX_SIZE_MB)

    if file.content_type not in ALLOWED_TYPES:
        raise InvalidFormatError()

    content = await file.read()

    if len(content) > MAX_SIZE_MB * 1024 * 1024:
        raise FileTooLargeError(MAX_SIZE_MB)

    extractor = PDFClient()
    use_case = ExtractTextUseCase(extractor)

    result = use_case.execute(
        file_content=content,
        filename=file.filename or "document.pdf",
    )

    return PDFUploadResponse(
        file_id=result.file_id,
        filename=file.filename or "document.pdf",
        checksum=result.checksum,
        text_preview=result.text[:500],
        is_duplicate=False,
    )