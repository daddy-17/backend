from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import users, admin, wallet, purchases, datamart

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="DataMart Store API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://datahubgh.pages.dev"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(wallet.router, prefix="/wallet", tags=["Wallet"])
app.include_router(purchases.router, prefix="/purchases", tags=["Purchases"])
app.include_router(datamart.router, prefix="/datamart", tags=["DataMart"])
