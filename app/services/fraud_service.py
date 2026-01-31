from app.database import SessionLocal
from app.models.transaction import Transaction
from sqlalchemy.orm import Session

def analyze_transaction(data):
    risk = "LOW"
    reasons = []

    if data.amount > 10000:
        risk = "HIGH"
        reasons.append("High transaction amount")

    if data.country != "BR":
        if risk != "HIGH":
            risk = "MEDIUM"
        reasons.append("International transaction")

    db = SessionLocal()

    transaction = Transaction(
        user_id=data.user_id,
        amount=data.amount,
        country=data.country,
        risk=risk
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    db.close()

    return {
        "id": transaction.id,
        "user_id": data.user_id,
        "amount": data.amount,
        "country": data.country,
        "risk": risk,
        "reasons": reasons
    }

def get_fraud_history():
    db: Session = SessionLocal()

    transactions = db.query(Transaction).all()

    result = []
    for t in transactions:
        result.append({
            "id": t.id,
            "user_id": t.user_id,
            "amount": t.amount,
            "country": t.country,
            "risk": t.risk
        })

    db.close()
    return result