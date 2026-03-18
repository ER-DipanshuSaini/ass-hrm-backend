from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.middlewares.error_handler import global_exception_handler
from app.modules.employees.router import router as employees_router
from app.modules.attendance.router import router as attendance_router
from app.modules.reports.router import router as reports_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HRMS Lite API",
    description="Lightweight Human Resource Management System REST API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(Exception, global_exception_handler)

app.include_router(employees_router, prefix="/api")
app.include_router(attendance_router, prefix="/api")
app.include_router(reports_router, prefix="/api")

@app.get("/health", tags=["default"], summary="Health Check")
def health_check():
    return {"status": "ok"}

@app.get("/", tags=["default"], summary="Root")
def root():
    return {"status": "success", "message": "HRMS API is running smoothly!"}
