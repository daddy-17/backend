import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

DATABASE_URL = DATABASE_URL or "sqlite:///./data.db"
JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
DATAMART_API_KEY = os.getenv("DATAMART_API_KEY")
DATAMART_BASE_URL = "https://api.datamartgh.shop/api/developer"
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
