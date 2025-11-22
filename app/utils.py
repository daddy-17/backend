import requests
from app.config import PAYSTACK_SECRET_KEY, DATAMART_API_KEY, DATAMART_BASE_URL

# Paystack
def verify_paystack_payment(reference):
    url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {"Authorization": f"Bearer {PAYSTACK_SECRET_KEY}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    if res["status"] and res["data"]["status"] == "success":
        return res["data"]["amount"] / 100  # convert kobo to Naira
    return None

# DataMart API
def datamart_get(endpoint, params={}):
    headers = {"X-API-Key": DATAMART_API_KEY}
    res = requests.get(f"{DATAMART_BASE_URL}/{endpoint}", headers=headers, params=params)
    return res.json()

def datamart_post(endpoint, payload):
    headers = {"X-API-Key": DATAMART_API_KEY, "Content-Type": "application/json"}
    res = requests.post(f"{DATAMART_BASE_URL}/{endpoint}", headers=headers, json=payload)
    return res.json()
