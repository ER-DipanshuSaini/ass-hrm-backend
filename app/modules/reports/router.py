from fastapi import APIRouter
from app.schemas import ResponseSchema

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/summary", response_model=ResponseSchema)
def get_reports_summary():
    return ResponseSchema(message="Reporting module is under development")
