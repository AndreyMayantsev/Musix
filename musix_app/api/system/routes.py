from fastapi import APIRouter, Response, Depends
from musix_app.api.composer import BaseResponse
from musix_app.dependencies import get_server
from musix_app.app_server import AppServer
from musix_app.models.models import ApplicationModelCreate

system_router = APIRouter()


@system_router.get("/system", response_model=BaseResponse[dict])
def about_system(server: AppServer = Depends(get_server)):
    """
    Returns information about system
    """
    return server.system_service.make_response()


@system_router.get("/favicon.ico", include_in_schema=False)
def get_favicon(server: AppServer = Depends(get_server)):
    """
    Get favicon for browser
    """
    with open("icon.png", 'rb') as _favicon:
        favicon = _favicon.read()

    return Response(content=favicon, media_type="image/png")


@system_router.post("/apps/", response_model=BaseResponse, status_code=201)
def register_app(app: ApplicationModelCreate, server: AppServer = Depends(get_server)):
    """
    Register new app
    """
    id = server.app_service.register_app(os=app.os, name=app.name, info=app.info)
    return {"data": {"reg_status": True, "app": id }}
