from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.routers import auth, user, category, product, cart

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EcoFinds API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(user.router, prefix="/api", tags=["Users"])
app.include_router(category.router, prefix="/api", tags=["Categories"])
app.include_router(product.router, prefix="/api", tags=["Products"])
app.include_router(cart.router, prefix="/api", tags=["Cart"])

@app.get("/")
def root():
    return {"message": "Welcome to the EcoFinds API"}