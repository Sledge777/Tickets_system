from sqlalchemy import select

from data_baze.db import Session, engine, Base
from data_baze.models import Employee_ORM
from models import Employee


def add(employee: Employee):
    with Session() as session:
        employee_orm = Employee_ORM(
            name=employee.name,
            department_id=employee.department_id,
            role=employee.role
        )
        session.add(employee_orm)
        session.commit()
        session.refresh(employee_orm)
        return "Employee created successfully with ID: {}".format(employee_orm.id)
    

def all():
    with Session() as session:
        result = session.execute(select(Employee_ORM)).scalars().all()
        return [Employee(
            id=employee.id,
            name=employee.name,
            department_id=employee.department_id,
            role=employee.role
        ) for employee in result]
    
    
def by_id(employee_id: int):
    with Session() as session:
        result = session.execute(select(Employee_ORM).where(Employee_ORM.id == employee_id)).scalar_one_or_none()
        if result:
            return Employee(
                id=result.id,
                name=result.name,
                department_id=result.department_id,
                role=result.role
            )
        else:
            return None
        
def remove(employee_id: int):
    with Session() as session:
        employee = session.execute(select(Employee_ORM).where(Employee_ORM.id == employee_id)).scalar_one_or_none()
        if employee:
            session.delete(employee)
            session.commit()
            return "Employee with ID {} removed successfully.".format(employee_id)
        else:
            return "Employee with ID {} not found.".format(employee_id)
