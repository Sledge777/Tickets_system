from fastapi import APIRouter, HTTPException

from data_baze.requests import add_ticket, all_tickets, ticket_by_id, remove_ticket

from models import Ticket

router = APIRouter(prefix="/ticet", tags=["ticket🎫"])



@router.get("/all")
async def get_all_tickets():
    try:
        tickets = all_tickets()
        return tickets
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.post("/add")
async def post_ticket(model: Ticket):
    try:
        result = add_ticket(model)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/{ticket_id}")
async def get_ticket_by_id(ticket_id: int):
    try:
        ticket = ticket_by_id(ticket_id)
        if ticket:
            return ticket
        else:
            raise HTTPException(status_code=404, detail="Ticket not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int):
    try:
        result = remove_ticket(ticket_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

