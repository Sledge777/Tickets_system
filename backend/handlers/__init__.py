from fastapi import APIRouter

from handlers.ticket import router as ticket_router
from handlers.department import router as department_router
from handlers.spot import router as spot_router
from handlers.employee import router as employee_router


router = APIRouter()


router.include_router(ticket_router)
router.include_router(department_router)
router.include_router(spot_router)
router.include_router(employee_router)
# router.include_router()