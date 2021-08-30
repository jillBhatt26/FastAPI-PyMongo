# Imports
from pydantic import BaseModel
from typing import Optional


# Classes Definitions
class CreateFinance(BaseModel):
    title: str
    amount: float
    description: str
    category: str
    isDue: bool



class UpdateFinance(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None
    isDue: Optional[bool] = None