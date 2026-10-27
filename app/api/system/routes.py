from fastapi import APIRouter, Response
from app.services.system_service import SystemInfo
from app.api.composer import BaseResponse
from app.services.apps_service import AppInfo, _apps_store


system_router = APIRouter()


@system_router.get("/system", response_model=BaseResponse[dict])
def about_system():
    """ Returns information about system """
    return SystemInfo().make_response()


@system_router.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    """ Get favicon for browser """
    with open("icon.png", 'rb') as _favicon:
        favicon = _favicon.read()

    return Response(content=favicon, media_type="image/png")


@system_router.post("/apps/", response_model=BaseResponse)
def register_app(app: AppInfo):
    """ Register new app """
    _apps_store[app.id] = app
    return {"data": {"reg_status": True, "app": app.id }}

@system_router.get("/apps/:id", response_model=BaseResponse)
def register_app(id):
    """ Get app info by id """
    app_info = _apps_store[id]
    return {"data": {"app": app_info }}