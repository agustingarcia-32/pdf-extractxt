import hashlib
from dataclasses import dataclass


@dataclass
class ExtractTextResult:
    text: str
    checksum: str
    file_id: str


class ExtractTextUseCase:
    def __init__(self, pdf_extractor: "PDFExtractor"):
        self._extractor = pdf_extractor

    def execute(self, file_content: bytes, filename: str) -> ExtractTextResult:
        text = self._extractor.extract_text(file_content)
        checksum = hashlib.sha256(file_content).hexdigest()
        file_id = hashlib.md5(f"{filename}{checksum}".encode()).hexdigest()[:16]
        return ExtractTextResult(text=text, checksum=checksum, file_id=file_id)