from sqlalchemy import select

from data_baze.db import Session, engine, Base
from data_baze.models import Department_ORM
from models import Department


def add(department: Department):
    with Session() as session:
        department_orm = Department_ORM(
            name=department.name,
            description=department.description
        )
        session.add(department_orm)
        session.commit()
        session.refresh(department_orm)
        return "Department created successfully with ID: {}".format(department_orm.id)


def all():
    with Session() as session:
        result = session.execute(select(Department_ORM)).scalars().all()
        return [Department(
            id=department.id,
            name=department.name,
            description=department.description
        ) for department in result]
    
    
def by_id(department_id: int):
    with Session() as session:
        result = session.execute(select(Department_ORM).where(Department_ORM.id == department_id)).scalar_one_or_none()
        if result:
            return Department(
                id=result.id,
                name=result.name,
                description=result.description
            )
        else:
            return None
        
def remove(department_id: int):
    with Session() as session:
        department = session.execute(select(Department_ORM).where(Department_ORM.id == department_id)).scalar_one_or_none()
        if department:
            session.delete(department)
            session.commit()
            return "Department with ID {} removed successfully.".format(department_id)
        else:
            return "Department with ID {} not found.".format(department_id)
