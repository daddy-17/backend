from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.models import Transaction, User
from app.utils import verify_paystack_payment
import uuid

router = APIRouter()

# Deposit via Paystack
@router.post("/deposit")
def deposit(amount: float, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    reference = str(uuid.uuid4())
    tx = Transaction(
        user_id=current_user.id,
        amount=amount,
        type="deposit",
        status="pending",
        reference=reference
    )
    db.add(tx)
    db.commit()
    db.refresh(tx)
    # Frontend uses this reference to initiate Paystack checkout
    return {"reference": reference, "amount": amount}

# Verify Paystack payment
@router.post("/verify")
def verify_payment(reference: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    tx = db.query(Transaction).filter(Transaction.reference == reference, Transaction.user_id == current_user.id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if tx.status == "completed":
        return {"message": "Already verified"}
    paid_amount = verify_paystack_payment(reference)
    if paid_amount and paid_amount == tx.amount:
        tx.status = "completed"
        current_user.wallet_balance += paid_amount
        db.commit()
        return {"message": "Wallet credited successfully", "balance": current_user.wallet_balance}
    else:
        tx.status = "failed"
        db.commit()
        raise HTTPException(status_code=400, detail="Payment verification failed")
