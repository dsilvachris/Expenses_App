from pydantic import BaseModel, EmailStr, conint, conlist
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    mobile: str

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    split_method: str
    participants: List[dict]
