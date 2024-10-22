from sqlalchemy import Column, String, Integer, Float, Enum, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base
from enum import Enum as PyEnum

class SplitMethod(PyEnum):
    EQUAL = "equal"
    EXACT = "exact"
    PERCENTAGE = "percentage"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mobile = Column(String, unique=True, nullable=False)

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    split_method = Column(Enum(SplitMethod), nullable=False)
    participants = Column(JSON, nullable=False)  # Stores user contributions
