from sqlalchemy import Column, Integer, String, DateTime, Numeric
from datetime import datetime
from app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    amount = Column(Integer)
    category = Column(String)
    note = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)