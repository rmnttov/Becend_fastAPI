from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.config import settings
from src.route.notes import router as notes_router
from src.route.notes import router as users_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=f'{settings.BASE_ROUTE_PATH}/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['GET', 'POST', 'OPTIONS'],
)

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

router.include_router(notes_router, prefix='/note')
router.include_router(users_router, prefix='/user')

app.include_router(router)
