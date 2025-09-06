from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, sample

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
    return {'msg': 'Backend  is running  again 🚀'}
