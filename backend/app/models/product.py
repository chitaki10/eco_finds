# backend/app/models/product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    description = Column(String(1024))
    price = Column(Float, nullable=False)
    image_url = Column(String(255))
    
    # --- NEW FIELDS ---
    quantity = Column(Integer, default=1)
    condition = Column(String(50)) # e.g., "New", "Used - Like New"
    year_of_manufacture = Column(Integer, nullable=True)
    brand = Column(String(100), nullable=True)
    model = Column(String(100), nullable=True)
    dimensions = Column(String(100), nullable=True) # e.g., "10x5x2 cm"
    weight = Column(Float, nullable=True) # in kg
    material = Column(String(100), nullable=True)
    color = Column(String(50), nullable=True)
    original_packaging = Column(Boolean, default=False)
    manual_included = Column(Boolean, default=False)
    working_condition = Column(String(500))

    # --- RELATIONSHIPS ---
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="products")