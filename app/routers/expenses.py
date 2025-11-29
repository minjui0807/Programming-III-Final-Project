# app/routers/expenses.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app import deps
from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.services import expense_service, analysis_service

router = APIRouter(prefix="/expenses", tags=["記帳功能"])

@router.post("/", response_model=ExpenseResponse)
def create_expense(item: ExpenseCreate, db: Session = Depends(deps.get_db)):
    return expense_service.create_expense(db, item)

@router.get("/", response_model=List[ExpenseResponse])
def read_expenses(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return expense_service.get_expenses(db, skip, limit)

@router.get("/stats")
def get_expense_stats(
    type: str = Query("total", enum=["total", "average"]),
    db: Session = Depends(deps.get_db)
):
    """
    使用策略模式 (Strategy Pattern) 進行分析
    """
    all_expenses = expense_service.get_expenses(db)
    strategy = analysis_service.get_strategy(type)
    analyzer = analysis_service.ExpenseAnalyzer(strategy)
    result = analyzer.execute(all_expenses)
    return {"analysis_type": type, "result": result}

@router.get("/{expense_id}", response_model=ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(deps.get_db)):
    expense = expense_service.get_expense(db, expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(deps.get_db)):
    success = expense_service.delete_expense(db, expense_id)
    if not success:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"status": "ok"}
