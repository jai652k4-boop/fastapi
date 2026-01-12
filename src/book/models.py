from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.mysql import BINARY
from datetime import date, datetime, timezone
import uuid

class Book(SQLModel, table=True):
    
    __tablename__ = "books"
    
    id: bytes = Field(
        sa_column=Column(
            BINARY(16),
            primary_key=True,
            nullable=False,
            default=lambda: uuid.uuid4().bytes
        ))

    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field( default_factory=lambda: datetime.now(timezone.utc) )
    updated_at: datetime = Field( default_factory=lambda: datetime.now(timezone.utc) )

    def __repr__(self):
        return f"<Book {self.title}>"