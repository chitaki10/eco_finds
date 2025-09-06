# Database connection logic goes here
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Adjust with your credentials
DATABASE_URL = "mysql+pymysql://hackathon_user:strongpassword@localhost:3306/ecofinds_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
