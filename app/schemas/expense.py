from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 基礎欄位
class ExpenseBase(BaseModel):
    item_name: str
    amount: int
    category: str
    note: Optional[str] = None

# 建立時需要的欄位 (與 Base 相同)
class ExpenseCreate(ExpenseBase):
    pass

# 回傳給前端的欄位 (包含 ID 和 時間)
class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 用法 (舊版為 orm_mode = True)