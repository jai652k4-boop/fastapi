from pydantic import BaseModel, Field
from datetime import date
import uuid

class userModel(BaseModel):
    id: uuid.UUID
    username: str
    email: str
    password_hash: str = Field(exclude=True)
    is_verified: bool = Field(default=False)
    created_at: date
    updated_at: date
    
class UserCreateModel(BaseModel):
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=8)