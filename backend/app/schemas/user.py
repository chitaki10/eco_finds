# backend/app/schemas/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for returning user data (omits password)
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    # Add other fields you might want to display
    # other_info: Optional[str] = None 

    class Config:
        from_attributes = True

# Schema for updating user data
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    # You could add other fields here like 'other_info'