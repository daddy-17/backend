from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Transaction, Bundle
from app.auth import get_current_user
from app.utils import datamart_post
import uuid

router = APIRouter()

@router.post("/")
def purchase_data(bundle_id: int, phone_number: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    bundle = db.query(Bundle).filter(Bundle.id == bundle_id).first()
    if not bundle:
        raise HTTPException(status_code=404, detail="Bundle not found")
    if current_user.wallet_balance < bundle.price:
        raise HTTPException(status_code=400, detail="Insufficient wallet balance")
    
    # Prepare DataMart purchase
    payload = {
        "phoneNumber": phone_number,
        "network": bundle.network,
        "capacity": bundle.capacity,
        "gateway": "wallet"
    }
    response = datamart_post("purchase", payload)
    if response.get("status") != "success":
        raise HTTPException(status_code=400, detail=response.get("message", "Purchase failed"))

    # Deduct from wallet
    current_user.wallet_balance -= bundle.price
    tx = Transaction(
        user_id=current_user.id,
        amount=bundle.price,
        type="purchase",
        status="completed",
        reference=str(uuid.uuid4())
    )
    db.add(tx)
    db.commit()
    return {"message": "Purchase successful", "bundle": bundle, "transaction": tx.id}
