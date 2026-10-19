from fastapi import APIRouter, Response
from app.services.system_service import SystemInfo
from app.api.composer import BaseResponse
from app.services.apps_service import AppInfo, _apps_store


system_router = APIRouter()


@system_router.get("/system", response_model=BaseResponse[dict])
def about_system():
    return SystemInfo().make_response()


@system_router.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    with open("icon.png", 'rb') as _favicon:
        favicon = _favicon.read()

    return Response(content=favicon, media_type="image/png")


@system_router.post("/register_app", response_model=BaseResponse)
def register_app(app: AppInfo):
    _apps_store[app.id] = app
    return {"data": {"reg_status": True, "app": app.id }}
