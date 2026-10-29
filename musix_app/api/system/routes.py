from fastapi import APIRouter, Response, Depends
from musix_app.api.composer import BaseResponse
from musix_app.dependencies import get_server
from musix_app.services.apps_service import AppInfo
from musix_app.app_server import AppServer


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


@system_router.post("/apps/", response_model=BaseResponse)
def register_app(app: AppInfo, server: AppServer = Depends(get_server)):
    """
    Register new app
    """
    server.app_service.register_app(app.id, app.info)
    return {"data": {"reg_status": True, "app": app.id }}

@system_router.get("/apps/{path:path}", response_model=BaseResponse)
def register_app(path, server: AppServer = Depends(get_server)):
    """
    Get app info by id
    """
    return {"data": {"app": server.app_service.get_registered_app(path)}}