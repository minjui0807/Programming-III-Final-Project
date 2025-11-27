from fastapi import FastAPI
from app.database import Base, engine
from app.routers import expenses
from app.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    # 自動建立資料表（真實專案用 Alembic）
    Base.metadata.create_all(bind=engine)

    # 掛載 Router
    app.include_router(expenses.router, prefix="/api/v1")

    @app.get("/")
    def root():
        return {"message": "System is running. Go to /docs for API."}

    return app


app = create_app()


'''
啟動在終端機輸入:uvicorn app.main:app --reload

expense的意思是 支出/開銷，這是記帳系統所以變數都用expense
'''