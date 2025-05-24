from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class DocumentType(str, Enum):
    POLICY = "policy"
    FAQ = "faq"
    PRODUCT = "product"
    SERVICE = "service"

class KnowledgeDocument(BaseModel):
    id: str
    filename: str
    type: DocumentType
    uploader_id: str
    upload_date: datetime
    vector_ids: list[str]
    source_path: str

    class Config:
        from_attributes = True
