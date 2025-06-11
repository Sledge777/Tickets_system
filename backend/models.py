from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    title: str
    description: str
    spot_id: int
    department: int
    type: str
    status: str
    created_at: str # d/m/y time

class Spot(BaseModel):
    id: int
    name: str
    location: str

class Department(BaseModel):
    id: int
    name: str
    description: str
    
class Employee(BaseModel):
    id: int
    name: str
    department_id: int
    role: str

