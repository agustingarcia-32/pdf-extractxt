from fastapi import HTTPException, status


class PDFValidationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
        )


class DuplicateDocumentError(HTTPException):
    def __init__(self, file_id: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "error": "duplicate_document",
                "existing_file_id": file_id,
                "message": "PDF con este checksum ya existe",
            },
        )


class FileTooLargeError(HTTPException):
    def __init__(self, max_size_mb: int):
        super().__init__(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail={
                "error": "file_too_large",
                "max_size_mb": max_size_mb,
                "message": f"El archivo excede el tamaño máximo de {max_size_mb}MB",
            },
        )


class InvalidFormatError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail={
                "error": "invalid_format",
                "allowed_types": ["application/pdf"],
                "message": "Solo se aceptan archivos PDF",
            },
        )