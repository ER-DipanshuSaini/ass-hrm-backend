from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas import ResponseSchema
from app.modules.attendance.schemas import AttendanceCreate, AttendanceResponse
from app.modules.attendance.controller import AttendanceController

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.get("/", response_model=ResponseSchema[List[AttendanceResponse]], summary="List attendance records")
def get_all_attendance(db: Session = Depends(get_db)):
    records = AttendanceController.get_all(db)
    return ResponseSchema(data=records)

@router.post("/", response_model=ResponseSchema[AttendanceResponse], summary="Mark Attendance")
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    record = AttendanceController.mark_attendance(data, db)
    return ResponseSchema(message="Attendance marked successfully", data=record)

@router.delete("/{id}", response_model=ResponseSchema, summary="Delete Attendance")
def delete_attendance(id: int, db: Session = Depends(get_db)):
    res = AttendanceController.delete_record(id, db)
    return ResponseSchema(message=res["message"])
