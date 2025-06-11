from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from data_baze.db import Base

class Ticket_ORM(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    spot_id: Mapped[int] = mapped_column(ForeignKey("spot.id"))
    department: Mapped[int] = mapped_column(ForeignKey("department.id"))
    type: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    created_at: Mapped[str] = mapped_column()  # d/m/y time



class Spot_ORM(Base):
    __tablename__ = "spot"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    location: Mapped[str] = mapped_column()


class Department_ORM(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()


class Employee_ORM(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    role: Mapped[str] = mapped_column()