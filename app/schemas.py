from datetime import date
from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    pub_date: Optional[date] 

class User(BaseModel):
    user: str
    password: str

