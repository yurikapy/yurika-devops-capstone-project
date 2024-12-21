import os
from sqlalchemy import create_engine

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:yourpassword@localhost:5432/yourdbname"
)

engine = create_engine(DATABASE_URI)

try:
    connection = engine.connect()
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
