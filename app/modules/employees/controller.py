from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.modules.employees.schemas import EmployeeCreate
from app.modules.employees.service import EmployeeService

class EmployeeController:
    @staticmethod
    def create_employee(data: EmployeeCreate, db: Session):
        if EmployeeService.get_by_emp_id(db, data.employee_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Employee ID already exists")
        if EmployeeService.get_by_email(db, data.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        return EmployeeService.create(db, data)
        
    @staticmethod
    def get_employee_by_id(db_id: int, db: Session):
        emp = EmployeeService.get_by_id(db, db_id)
        if not emp:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return emp

    @staticmethod
    def update_employee(db_id: int, data: EmployeeCreate, db: Session):
        existing = EmployeeService.get_by_id(db, db_id)
        if not existing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
            
        emp_by_id = EmployeeService.get_by_emp_id(db, data.employee_id)
        if emp_by_id and emp_by_id.id != db_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Employee ID already exists")
            
        emp_by_email = EmployeeService.get_by_email(db, data.email)
        if emp_by_email and emp_by_email.id != db_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
            
        return EmployeeService.update(db, db_id, data)

    @staticmethod
    def get_all_employees(db: Session):
        return EmployeeService.get_all(db)

    @staticmethod
    def delete_employee(db_id: int, db: Session):
        success = EmployeeService.delete(db, db_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return {"message": "Employee deleted successfully"}
