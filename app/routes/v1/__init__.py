from fastapi import APIRouter
from app.routes.v1.ping_route import router as ping_router


routers = APIRouter(prefix="/v1")
router_list = [ping_router]

for router in router_list:
    routers.include_router(router)

__all__ = ["routers"]