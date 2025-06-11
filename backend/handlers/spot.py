from fastapi import APIRouter, HTTPException
from data_baze.requests import add_spot, all_spots, spot_by_id, remove_spot
from models import Spot


router = APIRouter(prefix="/spot", tags=["spot📍"])

@router.get("/all")
async def get_all_spots():
    try:
        spots = all_spots()
        return spots
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/add")
async def post_spot(model: Spot):
    try:
        result = add_spot(model)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.get("/{spot_id}")
async def get_spot_by_id(spot_id: int):
    try:
        spot = spot_by_id(spot_id)
        if spot:
            return spot
        else:
            raise HTTPException(status_code=404, detail="Spot not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.delete("/{spot_id}")
async def delete_spot(spot_id: int):
    try:
        result = remove_spot(spot_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))