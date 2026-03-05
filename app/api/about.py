from app.baseapp.system_info import get_system_info
from .composer import ResponseType, compose_response


class SystemInfo:
    # About system

    def __init__(self):
        self.system = get_system_info()
        self.headers = {}

    def make_response(self):
        resp = {
            "OS": self.system.OS_NAME,
            "Host": self.system.HOST_NAME,
            "user": self.system.USER_NAME,
            "user_home": self.system.USER_HOME,
            "processor": self.system.PROCESSOR_INFO
        }
        return compose_response(ResponseType.OK, resp)


