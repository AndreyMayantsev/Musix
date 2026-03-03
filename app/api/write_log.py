from app.baseapp.system_info import get_system_info
from .composer import ResponseType, compose_response


class WriteLog:

    def __init__(self):
        self.system = get_system_info()
        self.headers = {}

    def make_response(self):
        resp = {
            "writing": "ok"
        }
        return compose_response(ResponseType.OK, resp)
