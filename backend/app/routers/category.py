# backend/app/routers/category.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# --- Local Imports (CORRECTED) ---
from app.dependencies import get_db # Import get_db from the correct file
from app.models.category import Category
from app.schemas.category import Category as CategorySchema

router = APIRouter()

@router.get("/categories", response_model=List[CategorySchema])
def get_all_categories(db: Session = Depends(get_db)): # This now works correctly
    """
    Get a list of all product categories.
    """
    return db.query(Category).order_by(Category.name).all()