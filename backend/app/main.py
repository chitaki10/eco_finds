from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, sample

# --- NEW IMPORTS ---
from app.db.database import Base, engine
from app.models import user # Import your models so SQLAlchemy knows about them

# --- NEW CODE ---
# This line creates the database tables if they don't exist.
# It uses the engine to connect to the database and Base to find all the table models.
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

@app.get('/')
def root():
    return {'msg': 'Backend running successfully 🚀'}