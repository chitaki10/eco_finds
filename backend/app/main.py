from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# --- CHANGE IS HERE: Import the product router with an alias ---
from app.routers import auth, sample, product as product_router

# --- NEW IMPORTS (These are correct) ---
from app.db.database import Base, engine
from app.models import user, product, category

# This line creates the database tables if they don't exist.
Base.metadata.create_all(bind=engine)


app = FastAPI(title='Hackathon Platform')

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router, prefix='/api/auth', tags=['Auth'])
app.include_router(sample.router, prefix='/api/sample', tags=['Sample'])

# --- CHANGE IS HERE: Use the new alias 'product_router' ---
app.include_router(product_router.router, prefix='/api', tags=['Products'])


@app.get('/')
def root():
    return {'msg': 'Backend running successfully 🚀'}

# Near the top with other router imports
from app.routers import auth, sample, product as product_router, category as category_router, user as user_router

# Near the bottom where you include other routers
app.include_router(user_router.router, prefix='/api', tags=['Users'])