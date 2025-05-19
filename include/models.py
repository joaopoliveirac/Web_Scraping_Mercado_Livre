from sqlalchemy import Column, String, Integer, Float, DateTime
from .db import Base
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True)
    title = Column(String)
    old_price = Column(Float)
    new_price = Column(Float)
    discount = Column(Float)
    link = Column(String)
    date = Column(DateTime, default = datetime.utcnow)

