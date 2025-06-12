from fastapi import APIRouter, HTTPException
from data_baze.db_requests import spot
from models import Spot


router = APIRouter(prefix="/spot", tags=["spot📍"])

@router.get("/all")
async def get_all_spots():
    try:
        spots = spot.all()
        return spots
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/add")
async def post_spot(model: Spot):
    try:
        result = spot.add(model)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

@router.get("/{spot_id}")
async def get_spot_by_id(spot_id: int):
    try:
        result = spot.by_id(spot_id)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Spot not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{spot_id}")
async def delete_spot(spot_id: int):
    try:
        result = spot.remove(spot_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))