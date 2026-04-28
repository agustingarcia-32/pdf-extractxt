from datetime import datetime
from typing import Optional


class PDFDocument:
    def __init__(
        self,
        file_id: str,
        filename: str,
        checksum: str,
        text: str,
        created_at: Optional[datetime] = None,
    ):
        self.file_id = file_id
        self.filename = filename
        self.checksum = checksum
        self.text = text
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self) -> dict:
        return {
            "file_id": self.file_id,
            "filename": self.filename,
            "checksum": self.checksum,
            "text": self.text,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PDFDocument":
        return cls(
            file_id=data["file_id"],
            filename=data["filename"],
            checksum=data["checksum"],
            text=data["text"],
            created_at=data.get("created_at"),
        )