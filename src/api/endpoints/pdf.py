from fastapi import APIRouter, File, UploadFile
from pymongo import MongoClient
from bson import ObjectId

from src.api.errors import FileTooLargeError, InvalidFormatError
from src.api.schemas import PDFUploadResponse
from src.core.use_cases.extract_text import ExtractTextUseCase
from src.infrastructure.pdf_client.client import PDFClient

router = APIRouter(prefix="/pdf", tags=["PDF"])

MAX_SIZE_MB = 10
ALLOWED_TYPES = {"application/pdf"}

client = MongoClient("mongodb://localhost:27017")
db = client["pdf_extractxt"]
collection = db["documents"]


# -------------------------------
# POST /pdf/extract
# -------------------------------
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

    existing_document = collection.find_one({"checksum": result.checksum})

    if existing_document:
        return PDFUploadResponse(
            file_id=str(existing_document["_id"]),
            filename=existing_document["filename"],
            checksum=existing_document["checksum"],
            text_preview=existing_document["text"][:500],
            is_duplicate=True,
        )

    inserted = collection.insert_one({
        "filename": file.filename or "document.pdf",
        "checksum": result.checksum,
        "text": result.text,
    })

    return PDFUploadResponse(
        file_id=str(inserted.inserted_id),
        filename=file.filename or "document.pdf",
        checksum=result.checksum,
        text_preview=result.text[:500],
        is_duplicate=False,
    )


# -------------------------------
# GET /pdf/documents
# -------------------------------
@router.get("/documents")
def get_documents():
    docs = []
    for doc in collection.find():
        docs.append({
            "id": str(doc["_id"]),
            "filename": doc["filename"],
            "checksum": doc["checksum"]
        })
    return docs


# -------------------------------
# GET /pdf/documents/{doc_id}
# -------------------------------
@router.get("/documents/{doc_id}")
def get_document(doc_id: str):
    try:
        doc = collection.find_one({"_id": ObjectId(doc_id)})
    except:
        return {"error": "ID inválido"}

    if not doc:
        return {"error": "Documento no encontrado"}

    return {
        "id": str(doc["_id"]),
        "filename": doc["filename"],
        "checksum": doc["checksum"],
        "text": doc["text"]
    }


# -------------------------------
# DELETE /pdf/documents/{doc_id}
# -------------------------------
@router.delete("/documents/{doc_id}")
def delete_document(doc_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(doc_id)})
    except:
        return {"error": "ID inválido"}

    return {"deleted": result.deleted_count}