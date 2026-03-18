from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.modules.attendance.schemas import AttendanceCreate
from app.modules.attendance.service import AttendanceService
from app.modules.employees.service import EmployeeService

class AttendanceController:
    @staticmethod
    def mark_attendance(data: AttendanceCreate, db: Session):
        emp = EmployeeService.get_by_id(db, data.employee_id)
        if not emp:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return AttendanceService.upsert(db, data)
        
    @staticmethod
    def get_all(db: Session):
        return AttendanceService.get_all(db)

    @staticmethod
    def delete_record(db_id: int, db: Session):
        success = AttendanceService.delete(db, db_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
        return {"message": "Attendance record deleted"}
