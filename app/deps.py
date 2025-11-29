'''
建立一個 SessionLocal() 資料庫連線

把連線用 yield 傳出去（讓 FastAPI 依賴注入使用）

在使用完後自動 db.close()
'''
from typing import Generator
from app.database import SessionLocal

def get_db() -> Generator:
    """
    建立一個 SessionLocal() 資料庫連線
    把連線用 yield 傳出去（讓 FastAPI 依賴注入使用）
    使用完後自動 db.close()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
