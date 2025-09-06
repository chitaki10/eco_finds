# backend/app/schemas/product.py
from pydantic import BaseModel
from .category import Category

# New Schema for creating a product
class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    category_id: int
    quantity: int = 1
    condition: str
    # Add other fields as needed, keeping them optional if they can be empty
    brand: str | None = None
    model: str | None = None
    working_condition: str

# This is the existing schema for returning a product
class Product(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None
    category: Category
    condition: str | None = None
    brand: str | None = None
    
    class Config:
        from_attributes = True