from sqlalchemy import Column, Integer, Date, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Session, relationship
from app.core.database import Base
from app.modules.attendance.schemas import AttendanceCreate, AttendanceStatus
from app.modules.employees.service import Employee 

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(SQLEnum(AttendanceStatus), nullable=False)

    employee = relationship("Employee", back_populates="attendances")

class AttendanceService:
    @staticmethod
    def get_by_emp_and_date(db: Session, emp_id: int, date_val):
        return db.query(Attendance).filter(
            Attendance.employee_id == emp_id,
            Attendance.date == date_val
        ).first()
        
    @staticmethod
    def get_all(db: Session):
        return db.query(Attendance).order_by(Attendance.date.desc()).all()

    @staticmethod
    def upsert(db: Session, data: AttendanceCreate):
        existing = AttendanceService.get_by_emp_and_date(db, data.employee_id, data.date)
        if existing:
            existing.status = data.status
            db.commit()
            db.refresh(existing)
            return existing
            
        new_att = Attendance(**data.model_dump())
        db.add(new_att)
        db.commit()
        db.refresh(new_att)
        return new_att
        
    @staticmethod
    def delete(db: Session, db_id: int):
        record = db.query(Attendance).filter(Attendance.id == db_id).first()
        if record:
            db.delete(record)
            db.commit()
            return True
        return False
