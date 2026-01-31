from pydantic import BaseModel

class TransactionRequest(BaseModel):
    user_id: int
    amount: float
    country: str
