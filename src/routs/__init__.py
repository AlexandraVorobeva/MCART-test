from fastapi import APIRouter
from .currency import router as currency_router

router = APIRouter()
router.include_router(currency_router)