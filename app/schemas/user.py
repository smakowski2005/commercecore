from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: str|None = None

    model_config = ConfigDict(from_attributes=True)
class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    first_name: str
    last_name: str
    phone: str|None = None
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)