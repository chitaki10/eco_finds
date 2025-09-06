from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    purchase_price = Column(DECIMAL(10, 2), nullable=False)
    purchase_date = Column(TIMESTAMP, server_default=func.now())
    
    user = relationship("User", back_populates="purchases")
    product = relationship("Product")