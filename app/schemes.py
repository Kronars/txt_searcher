from pydantic import BaseModel
from datetime import datetime

class TextSearch(BaseModel):
    text: str

class FoundedRow(BaseModel):
    index: int
    text: str
    rubrics: list[str]
    created_date: datetime

class TextFound(BaseModel):
    founded: list[FoundedRow]