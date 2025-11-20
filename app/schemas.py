from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    role: str
    wallet_balance: float
    created_at: datetime

    class Config:
        orm_mode = True

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

# Transaction schema
class TransactionBase(BaseModel):
    amount: float
    type: str
    status: str
    reference: str

class TransactionOut(TransactionBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Bundle schema
class BundleBase(BaseModel):
    network: str
    capacity: str
    mb: int
    price: float

class BundleOut(BundleBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
