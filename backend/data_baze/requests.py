import datetime

from sqlalchemy import select

from data_baze.db import Session, engine, Base
from data_baze.models import Ticket_ORM, Spot_ORM, Department_ORM, Employee_ORM
from models import Ticket, Spot, Department, Employee


def create_all_tables():
    Base.metadata.create_all(engine)

#__TICKETS OPERATIONS__

def add_ticket(ticket: Ticket):
    with Session() as session:
        ticket_orm = Ticket_ORM(
            title=ticket.title,
            description=ticket.description,
            spot_id=ticket.spot_id,
            department=ticket.department,
            type=ticket.type,
            status=ticket.status,
            created_at=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
        session.add(ticket_orm)
        session.commit()
        session.refresh(ticket_orm)
        return "Ticket created successfully with ID: {}".format(ticket_orm.id)
    

def all_tickets():
    with Session() as session:
        result = session.execute(select(Ticket_ORM))
        tickets = result.scalars().all()
        return tickets
    

def ticket_by_id(ticket_id: int):
    with Session() as session:
        result = session.execute(select(Ticket_ORM).where(Ticket_ORM.id == ticket_id)).scalar_one_or_none()
        if result:
            return Ticket(
                id=result.id,
                title=result.title,
                description=result.description,
                spot_id=result.spot_id,
                department=result.department,
                type=result.type,
                status=result.status,
                created_at=result.created_at
            )
        else:
            return None
        
def remove_ticket(ticket_id: int):
    with Session() as session:
        ticket = session.execute(select(Ticket_ORM).where(Ticket_ORM.id == ticket_id)).scalar_one_or_none()
        if ticket:
            session.delete(ticket)
            session.commit()
            return "Ticket with ID {} removed successfully.".format(ticket_id)
        else:
            return "Ticket with ID {} not found.".format(ticket_id)
        

#__SPOTS OPERATIONS__

def add_spot(spot: Spot):
    with Session() as session:
        spot_orm = Spot_ORM(
            name=spot.name,
            location=spot.location
        )
        session.add(spot_orm)
        session.commit()
        session.refresh(spot_orm)
        return "Spot created successfully with ID: {}".format(spot_orm.id)
    

def all_spots():
    with Session() as session:
        result = session.execute(select(Spot_ORM)).scalars().all()
        return [Spot(
            id=spot.id,
            name=spot.name,
            location=spot.location
        ) for spot in result]
    

def spot_by_id(spot_id: int):
    with Session() as session:
        result = session.execute(select(Spot_ORM).where(Spot_ORM.id == spot_id)).scalar_one_or_none()
        if result:
            return Spot(
                id=result.id,
                name=result.name,
                location=result.location
            )
        else:
            return None
        
def remove_spot(spot_id: int):
    with Session() as session:
        spot = session.execute(select(Spot_ORM).where(Spot_ORM.id == spot_id)).scalar_one_or_none()
        if spot:
            session.delete(spot)
            session.commit()
            return "Spot with ID {} removed successfully.".format(spot_id)
        else:
            return "Spot with ID {} not found.".format(spot_id)
        

#__DEPARTMENTS OPERATIONS__
def add_department(department: Department):
    with Session() as session:
        department_orm = Department_ORM(
            name=department.name,
            description=department.description
        )
        session.add(department_orm)
        session.commit()
        session.refresh(department_orm)
        return "Department created successfully with ID: {}".format(department_orm.id)


def all_departments():
    with Session() as session:
        result = session.execute(select(Department_ORM)).scalars().all()
        return [Department(
            id=department.id,
            name=department.name,
            description=department.description
        ) for department in result]
    
    
def department_by_id(department_id: int):
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
        
def remove_department(department_id: int):
    with Session() as session:
        department = session.execute(select(Department_ORM).where(Department_ORM.id == department_id)).scalar_one_or_none()
        if department:
            session.delete(department)
            session.commit()
            return "Department with ID {} removed successfully.".format(department_id)
        else:
            return "Department with ID {} not found.".format(department_id)
        
#__EMPLOYEES OPERATIONS__

def add_employee(employee: Employee):
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
    

def all_employees():
    with Session() as session:
        result = session.execute(select(Employee_ORM)).scalars().all()
        return [Employee(
            id=employee.id,
            name=employee.name,
            department_id=employee.department_id,
            role=employee.role
        ) for employee in result]
    
    
def employee_by_id(employee_id: int):
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
        
def remove_employee(employee_id: int):
    with Session() as session:
        employee = session.execute(select(Employee_ORM).where(Employee_ORM.id == employee_id)).scalar_one_or_none()
        if employee:
            session.delete(employee)
            session.commit()
            return "Employee with ID {} removed successfully.".format(employee_id)
        else:
            return "Employee with ID {} not found.".format(employee_id)
