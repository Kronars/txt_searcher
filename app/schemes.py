from datetime import datetime

from pydantic import BaseModel, constr


class TextSearch(BaseModel):
    text: constr(min_length=3)

class FoundedRow(BaseModel):
    index: int
    text: str
    rubrics: list[str]
    created_date: datetime

class TextFound(BaseModel):
    founded: list[FoundedRow]