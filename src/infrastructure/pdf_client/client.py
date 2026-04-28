import io
from typing import Optional

from pypdf import PdfReader


class PyPDFExtractor:
    def extract_text(self, file_content: bytes) -> str:
        reader = PdfReader(io.BytesIO(file_content))
        text_parts = []
        for page in reader.pages:
            text_parts.append(page.extract_text())
        return "\n".join(text_parts)


class PDFClient:
    def __init__(self):
        self._extractor = PyPDFExtractor()

    def extract_text(self, file_content: bytes) -> str:
        return self._extractor.extract_text(file_content)