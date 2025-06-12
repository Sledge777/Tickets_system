from sqlalchemy import select

from data_baze.db import Session, engine, Base
from data_baze.models import Spot_ORM
from models import Spot


def add(spot: Spot):
    with Session() as session:
        spot_orm = Spot_ORM(
            name=spot.name,
            location=spot.location
        )
        session.add(spot_orm)
        session.commit()
        session.refresh(spot_orm)
        return "Spot created successfully with ID: {}".format(spot_orm.id)
    

def all():
    with Session() as session:
        result = session.execute(select(Spot_ORM)).scalars().all()
        return [Spot(
            id=spot.id,
            name=spot.name,
            location=spot.location
        ) for spot in result]
    

def by_id(spot_id: int):
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
        
def remove(spot_id: int):
    with Session() as session:
        spot = session.execute(select(Spot_ORM).where(Spot_ORM.id == spot_id)).scalar_one_or_none()
        if spot:
            session.delete(spot)
            session.commit()
            return "Spot with ID {} removed successfully.".format(spot_id)
        else:
            return "Spot with ID {} not found.".format(spot_id)