from fastapi import APIRouter, HTTPException
from data_baze.requests import add_department, all_departments, department_by_id, remove_department
from models import Department

router = APIRouter(prefix="/department", tags=["department🏢"])

@router.get("/all")
async def get_all_departments():
    try:
        departments = all_departments()
        return departments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/add")
async def post_department(model: Department):
    try:
        result = add_department(model)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/{department_id}")
async def get_department_by_id(department_id: int):
    try:
        department = department_by_id(department_id)
        if department:
            return department
        else:
            raise HTTPException(status_code=404, detail="Department not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.delete("/{department_id}")
async def delete_department(department_id: int):
    try:
        result = remove_department(department_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
