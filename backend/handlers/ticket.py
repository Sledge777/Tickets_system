from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/ticet", tags=["ticket🎫"])



@router.get("/")
async def get_data():
    try:
        # Simulate data retrieval
        data = {"message": "Data retrieved successfully"}
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))