import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data.db")
JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
DATAMART_API_KEY = os.getenv("DATAMART_API_KEY")
DATAMART_BASE_URL = "https://api.datamartgh.shop/api/developer"
