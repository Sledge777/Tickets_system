from fastapi import APIRouter

from handlers.ticket import router as ticket_router


router = APIRouter()


router.include_router(ticket_router)
# router.include_router()