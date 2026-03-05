from flask import Blueprint
from app.api.about import SystemInfo

system_bp = Blueprint('system', __name__)


@system_bp.route("/system")
def about_system():
    return SystemInfo().make_response()
