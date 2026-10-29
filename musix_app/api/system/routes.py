from fastapi import APIRouter, Response, Depends
from musix_app.api.composer import BaseResponse
from musix_app.dependencies import get_server
from musix_app.services.apps_service import AppInfo, _apps_store
from musix_app.app_server import AppServer


system_router = APIRouter()


@system_router.get("/system", response_model=BaseResponse[dict])
def about_system(server: AppServer = Depends(get_server)):
    """ Returns information about system """
    return server.system_service.make_response()


@system_router.get("/favicon.ico", include_in_schema=False)
def get_favicon(server: AppServer = Depends(get_server)):
    """ Get favicon for browser """
    with open("icon.png", 'rb') as _favicon:
        favicon = _favicon.read()

    return Response(content=favicon, media_type="image/png")


@system_router.post("/apps/", response_model=BaseResponse)
def register_app(app: AppInfo, server: AppServer = Depends(get_server)):
    """ Register new app """
    _apps_store[app.id] = app
    return {"data": {"reg_status": True, "app": app.id }}

@system_router.get("/apps/:id", response_model=BaseResponse)
def register_app(id, server: AppServer = Depends(get_server)):
    """ Get app info by id """
    app_info = _apps_store[id]
    return {"data": {"app": app_info }}