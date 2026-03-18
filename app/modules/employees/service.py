from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, relationship
from app.core.database import Base
from app.modules.employees.schemas import EmployeeCreate

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, nullable=False)
    
    attendances = relationship("Attendance", back_populates="employee", cascade="all, delete-orphan")

class EmployeeService:
    @staticmethod
    def get_by_id(db: Session, db_id: int):
        return db.query(Employee).filter(Employee.id == db_id).first()

    @staticmethod
    def get_by_emp_id(db: Session, emp_id: str):
        return db.query(Employee).filter(Employee.employee_id == emp_id).first()
        
    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(Employee).filter(Employee.email == email).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Employee).order_by(Employee.id.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def create(db: Session, data: EmployeeCreate):
        db_obj = Employee(**data.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(db: Session, db_id: int, data: EmployeeCreate):
        db_obj = EmployeeService.get_by_id(db, db_id)
        if db_obj:
            db_obj.employee_id = data.employee_id
            db_obj.full_name = data.full_name
            db_obj.email = data.email
            db_obj.department = data.department
            db.commit()
            db.refresh(db_obj)
            return db_obj
        return None

    @staticmethod
    def delete(db: Session, db_id: int):
        db_obj = EmployeeService.get_by_id(db, db_id)
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False
