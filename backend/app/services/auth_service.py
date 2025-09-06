# backend/app/services/auth_service.py
from datetime import datetime, timedelta, timezone
from passlib.hash import bcrypt
from jose import JWTError, jwt

# Import our centralized settings
from app.core.config import settings

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against its hashed version."""
    return bcrypt.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    """Creates a new JWT access token."""
    to_encode = data.copy()

    # Calculate expiration time
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})

    # Encode the token
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )
    return encoded_jwt

# You can also add a token decoding function here for protected routes later
def decode_access_token(token: str):
    # This will be useful later for protecting endpoints
    try:
        payload = jwt.decode(
            token=token,
            key=settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )
        return payload
    except JWTError:
        return None