from abc import ABC, abstractmethod
from typing import Protocol


class PDFExtractor(Protocol):
    def extract_text(self, file_content: bytes) -> str:
        """Extract text from PDF content."""
        ...


class DocumentRepository(Protocol):
    async def save(self, document: "PDFDocument") -> None:
        """Save a document."""
        ...

    async def find_by_checksum(self, checksum: str) -> "PDFDocument | None":
        """Find document by checksum."""
        ...

    async def find_by_id(self, file_id: str) -> "PDFDocument | None":
        """Find document by ID."""
        ...