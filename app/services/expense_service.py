from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate
#在Swagger UI看到的畫面就是這裡

def get_expenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Expense).offset(skip).limit(limit).all()

def get_expense(db: Session, expense_id: int):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.model_dump()) #用model_dump()轉dict，再用**自動解包。等同於Expense(name=expense.name, description=expense.description, ...)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if db_expense:
        db.delete(db_expense)
        db.commit()
        return True
    return False