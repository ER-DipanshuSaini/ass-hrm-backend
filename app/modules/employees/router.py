from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas import ResponseSchema
from app.modules.employees.schemas import EmployeeCreate, EmployeeResponse
from app.modules.employees.controller import EmployeeController

router = APIRouter(prefix="/employees", tags=["Employee"])

@router.get("/", response_model=ResponseSchema[List[EmployeeResponse]], summary="List all employees")
def get_employees(db: Session = Depends(get_db)):
    emps = EmployeeController.get_all_employees(db)
    return ResponseSchema(data=emps)

@router.post("/", response_model=ResponseSchema[EmployeeResponse], status_code=status.HTTP_201_CREATED, summary="Create a new employee")
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    emp = EmployeeController.create_employee(data, db)
    return ResponseSchema(message="Employee created successfully", data=emp)

@router.get("/{employee_id}", response_model=ResponseSchema[EmployeeResponse], summary="Get employee by ID")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    emp = EmployeeController.get_employee_by_id(employee_id, db)
    return ResponseSchema(data=emp)

@router.put("/{employee_id}", response_model=ResponseSchema[EmployeeResponse], summary="Update employee")
def update_employee(employee_id: int, data: EmployeeCreate, db: Session = Depends(get_db)):
    emp = EmployeeController.update_employee(employee_id, data, db)
    return ResponseSchema(message="Employee updated successfully", data=emp)

@router.delete("/{employee_id}", response_model=ResponseSchema, summary="Delete employee")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    res = EmployeeController.delete_employee(employee_id, db)
    return ResponseSchema(message=res["message"])
