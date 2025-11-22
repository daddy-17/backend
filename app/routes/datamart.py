from fastapi import APIRouter, Depends
from app.utils import datamart_get
from app.auth import get_current_user

router = APIRouter()

# Get available bundles for a network
@router.get("/packages")
def get_packages(network: str = None):
    params = {"network": network} if network else {}
    return datamart_get("data-packages", params=params)

# Get transactions from DataMart API
@router.get("/transactions")
def get_transactions():
    return datamart_get("transactions")

# Claim referral bonuses
@router.post("/claim-referral")
def claim_referral():
    return datamart_post("claim-referral-bonus", {})
