from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import User, Expense
from app.schemas import UserCreate, ExpenseCreate
from app.database import get_db

router = APIRouter()

# Create a new user
@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Retrieve a user by ID
@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Add a new expense
@router.post("/expenses")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

# Retrieve expenses for a specific user
@router.get("/expenses/{user_id}")
def get_expenses_for_user(user_id: int, db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.participants.contains([{"user_id": user_id}])).all()
    return expenses
