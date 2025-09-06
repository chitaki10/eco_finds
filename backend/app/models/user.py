# backend/app/models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    # This column matches your schema: int, PK, auto_increment
    id = Column(Integer, primary_key=True, index=True)

    # --- UPDATED: Added String length to match VARCHAR(50) ---
    name = Column(String(50))

    # --- UPDATED: Added String length to match VARCHAR(120) ---
    email = Column(String(120), unique=True, index=True)

    # --- UPDATED: Added String length to match VARCHAR(255) ---
    hashed_password = Column(String(255))

    # This relationship links a user to the products they own. It does not create a column.
    products = relationship("Product", back_populates="owner")