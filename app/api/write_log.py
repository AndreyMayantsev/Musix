from app.baseapp.system_info import get_system_info


class WriteLog:
    # write local log

    def __init__(self):
        self.system = get_system_info()
        self.headers = {}

    def make_response(self):
        resp = {
            "writing": "ok"
        }
        return resp
