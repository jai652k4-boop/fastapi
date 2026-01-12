from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.mysql import BINARY
from datetime import datetime, date, timezone
import uuid

class User(SQLModel, table=True):

    __tablename__ = "users"

    id: bytes = Field(
        sa_column=Column(
            BINARY(16),
            primary_key=True,
            nullable=False,
            default=lambda: uuid.uuid4().bytes,
        )
    )
    
    username: str
    email: str = Field(unique=True)
    password_hash: str = Field(exclude=True)
    is_verified: bool = Field(default=False)
    created_at: date = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: date = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"< name {self.username} >"
