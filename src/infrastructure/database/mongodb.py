from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.core.entities.pdf_document import PDFDocument


class MongoDBClient:
    def __init__(self, uri: str, db_name: str):
        self._client: AsyncIOMotorClient | None = None
        self._uri = uri
        self._db_name = db_name

    async def connect(self) -> None:
        self._client = AsyncIOMotorClient(self._uri)

    async def disconnect(self) -> None:
        if self._client:
            self._client.close()

    @property
    def database(self) -> AsyncIOMotorDatabase:
        if not self._client:
            raise RuntimeError("Database not connected")
        return self._client[self._db_name]


class DocumentRepository:
    def __init__(self, db: MongoDBClient, collection_name: str):
        self._db = db
        self._collection_name = collection_name

    @property
    def collection(self):
        return self._db.database[self._collection_name]

    async def save(self, document: PDFDocument) -> None:
        await self.collection.insert_one(document.to_dict())

    async def find_by_checksum(self, checksum: str) -> PDFDocument | None:
        doc = await self.collection.find_one({"checksum": checksum})
        if doc:
            return PDFDocument.from_dict(doc)
        return None

    async def find_by_id(self, file_id: str) -> PDFDocument | None:
        doc = await self.collection.find_one({"file_id": file_id})
        if doc:
            return PDFDocument.from_dict(doc)
        return None