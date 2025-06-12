from fastapi import APIRouter, HTTPException
from data_baze.db_requests import department
from models import Department

router = APIRouter(prefix="/department", tags=["department🏢"])

@router.get("/all")
async def get_all_departments():
    try:
        departments = department.all()
        return departments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/add")
async def post_department(model: Department):
    try:
        result = department.add(model)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/{department_id}")
async def get_department_by_id(department_id: int):
    try:
        result = department.by_id(department_id)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.delete("/{department_id}")
async def delete_department(department_id: int):
    try:
        result = department.remove(department_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
