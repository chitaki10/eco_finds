# backend/app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.db.database import SessionLocal
from app.models.user import User

# NEW IMPORTS
from app.services.auth_service import verify_password, create_access_token

router = APIRouter()

# --- Existing RegisterRequest and get_db() can stay the same ---
class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Your existing /register endpoint stays the same ---
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(payload: RegisterRequest, db: Session = Depends(get_db)):
    if payload.password != payload.confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords do not match")

    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    hashed_pw = bcrypt.hash(payload.password)
    new_user = User(name=payload.name, email=payload.email, hashed_password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}


# =========================================================
# ===                  NEW LOGIN LOGIC                  ===
# =========================================================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/login")
def login_for_access_token(payload: LoginRequest, db: Session = Depends(get_db)):
    # 1. Find the user by email
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        # For security, we return a generic error to prevent email enumeration attacks
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 2. Verify the provided password against the stored hash
    if not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. If credentials are correct, create a JWT
    access_token = create_access_token(data={"sub": user.email, "user_id": user.id})

    # 4. Return the token
    return {"access_token": access_token, "token_type": "bearer"}