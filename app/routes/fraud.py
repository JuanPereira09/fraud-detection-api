from fastapi import APIRouter
from app.schemas.transaction import TransactionRequest
from app.services.fraud_service import analyze_transaction, get_fraud_history

router = APIRouter(
    prefix="/fraud",
    tags=["Fraud"]
)

@router.post("/analyze")
def analyze(data: TransactionRequest):
    return analyze_transaction(data)

@router.get("/history")
def history():
    return get_fraud_history()
