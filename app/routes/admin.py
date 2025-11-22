from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Bundle, Transaction
from app.auth import get_current_admin

router = APIRouter()

# List all users
@router.get("/users")
def list_users(admin = Depends(get_current_admin), db: Session = Depends(get_db)):
    return db.query(User).all()

# List all transactions
@router.get("/transactions")
def list_transactions(admin = Depends(get_current_admin), db: Session = Depends(get_db)):
    return db.query(Transaction).all()

# Create or update bundle
@router.post("/bundle")
def create_bundle(network: str, capacity: str, mb: int, price: float, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    bundle = Bundle(network=network, capacity=capacity, mb=mb, price=price)
    db.add(bundle)
    db.commit()
    db.refresh(bundle)
    return bundle

# Update bundle price
@router.put("/bundle/{bundle_id}/price")
def update_bundle_price(bundle_id: int, price: float, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    bundle = db.query(Bundle).filter(Bundle.id == bundle_id).first()
    if not bundle:
        raise HTTPException(status_code=404, detail="Bundle not found")
    bundle.price = price
    db.commit()
    return bundle
# Delete bundle
@router.delete("/bundle/{bundle_id}")
def delete_bundle(bundle_id: int, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    bundle = db.query(Bundle).filter(Bundle.id == bundle_id).first()
    if not bundle:
        raise HTTPException(status_code=404, detail="Bundle not found")
    db.delete(bundle)
    db.commit()
    return {"detail": "Bundle deleted"}