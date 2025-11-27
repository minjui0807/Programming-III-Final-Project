# Personal Expense Tracker API (個人記帳管理系統)

這是一個基於 **FastAPI** 與 **Python** 構建的後端 RESTful API 專案。
本專案採用嚴謹的 **分層架構 (Layered Architecture)**，實現了財務紀錄的 CRUD 操作，並運用 **策略模式 (Strategy Pattern)** 進行動態的財務統計分析，適合展示後端開發與軟體工程實力。

## 🚀 專案亮點 (Key Features)

- **現代化框架**：使用高效能的 FastAPI 框架與 Pydantic v2 進行資料驗證。
- **關注點分離 (SoC)**：將路由 (Routers)、商業邏輯 (Services)、資料模型 (Models/Schemas) 與資料庫操作嚴格分離，提升程式碼可維護性。
- **設計模式應用**：在統計功能 (`analysis_service.py`) 中實作 **策略模式 (Strategy Pattern)**，允許系統動態切換演算法（如總和、平均值），符合 **Open-Closed Principle (OCP)** 設計原則。
- **資料持久化**：整合 **SQLite** 與 **SQLAlchemy ORM**，支援系統啟動時自動建立資料表。
- **互動式文件**：內建 Swagger UI / OpenAPI 自動化文件。

## 🛠️ 技術堆疊 (Tech Stack)

- **Language**: Python 3.10+
- **Web Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic v2
- **Config Management**: pydantic-settings

## 📂 專案結構 (Project Structure)

本專案採用模組化設計，檔案結構如下：

```text
Programming-III-Final-Project/
├── app/
│   ├── models/          # SQLAlchemy ORM Models (資料庫結構定義)
│   │   └── expense.py
│   ├── routers/         # API Routes (路徑定義與 HTTP 請求處理)
│   │   └── expenses.py
│   ├── schemas/         # Pydantic Models (資料輸入/輸出驗證)
│   │   └── expense.py
│   ├── services/        # Business Logic (商業邏輯與 CRUD 實作)
│   │   ├── analysis_service.py  # [亮點] 策略模式實作
│   │   └── expense_service.py   # 記帳功能邏輯
│   ├── config.py        # 環境變數與全域設定
│   ├── database.py      # 資料庫連線與 Session 工廠
│   ├── deps.py          # 依賴注入 (Dependency Injection)
│   └── main.py          # 程式入口點 (Entry Point)
├── .env                 # 環境變數設定檔
├── expenses.db          # SQLite 資料庫檔案 (自動生成)
├── requirements.txt     # 專案依賴套件清單
└── README.md            # 專案說明文件