# backend/app/routers/product.py
from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from enum import Enum

# --- Local Imports (CORRECTED) ---
from app.dependencies import get_db, get_current_user # Import get_db from the correct file
from app.models.product import Product
from app.models.user import User
from app.schemas.product import Product as ProductSchema, ProductCreate

router = APIRouter()

# Enums for validated sorting options
class SortBy(str, Enum):
    name = "name"
    price = "price"

class SortDirection(str, Enum):
    asc = "asc"
    desc = "desc"

@router.get("/products", response_model=List[ProductSchema])
def get_products(
    db: Session = Depends(get_db), # This now works correctly
    search: Optional[str] = Query(None, description="Search for products by name or description"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    sort_by: Optional[SortBy] = Query(SortBy.name, description="Field to sort by"),
    sort_direction: Optional[SortDirection] = Query(SortDirection.asc, description="Sort direction (asc or desc)")
):
    query = db.query(Product)
    if search:
        query = query.filter(or_(Product.name.ilike(f"%{search}%"), Product.description.ilike(f"%{search}%")))
    if category_id:
        query = query.filter(Product.category_id == category_id)
    sort_column = getattr(Product, sort_by.value)
    if sort_direction == SortDirection.desc:
        sort_column = sort_column.desc()
    query = query.order_by(sort_column)
    return query.all()

@router.post("/products", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db), # This now works correctly
    current_user: User = Depends(get_current_user)
):
    new_product = Product(**product.model_dump(), owner_id=current_user.id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product