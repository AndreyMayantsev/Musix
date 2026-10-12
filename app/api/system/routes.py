from fastapi import APIRouter, Response, HTTPException
from app.api.about import SystemInfo

system_router = APIRouter()

@system_router.get("/system")
def about_system():
    return SystemInfo().make_response()

@system_router.get("/favicon.ico", include_in_schema=False)
def get_favicon():
    with open("icon.png", 'rb') as _favicon:
        favicon = _favicon.read()

    return Response(content=favicon, media_type="image/png")
