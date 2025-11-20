import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import Base, engine
from app.models import User, Transaction, Bundle  # Import all models

print("Creating database and tables...")
Base.metadata.create_all(bind=engine)
print("Database and tables created successfully.")