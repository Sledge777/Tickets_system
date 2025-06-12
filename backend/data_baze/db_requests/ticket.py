import datetime

from sqlalchemy import select

from data_baze.db import Session, engine, Base
from data_baze.models import Ticket_ORM
from models import Ticket


def add(ticket: Ticket):
    with Session() as session:
        ticket_orm = Ticket_ORM(
            title=ticket.title,
            description=ticket.description,
            spot_id=ticket.spot_id,
            department=ticket.department,
            type=ticket.type,
            status = False,  # Default status is False (not resolved)
            created_at=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
        session.add(ticket_orm)
        session.commit()
        session.refresh(ticket_orm)
        return "Ticket created successfully with ID: {}".format(ticket_orm.id)
    

def all():
    with Session() as session:
        result = session.execute(select(Ticket_ORM))
        tickets = result.scalars().all()
        return tickets
    

def by_id(ticket_id: int):
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
        
def remove(ticket_id: int):
    with Session() as session:
        ticket = session.execute(select(Ticket_ORM).where(Ticket_ORM.id == ticket_id)).scalar_one_or_none()
        if ticket:
            session.delete(ticket)
            session.commit()
            return "Ticket with ID {} removed successfully.".format(ticket_id)
        else:
            return "Ticket with ID {} not found.".format(ticket_id)