from fastapi import APIRouter, HTTPException
from data_baze.db_requests import employee
from models import Employee

router = APIRouter(prefix="/employee", tags=["employee👨‍💼"])


@router.get("/all")
async def get_all_employees():
    try:
        employees = employee.all()
        return employees
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add")
async def post_employee(model: Employee):
    try:
        result = employee.add(model)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{employee_id}")
async def get_employee_by_id(employee_id: int):
    try:
        result = employee.by_id(employee_id)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Employee not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{employee_id}")
async def delete_employee(employee_id: int):
    try:
        result = employee.remove(employee_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))