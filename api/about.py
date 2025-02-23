from baseapp.system_info import get_system_info
import json


class SystemInfo:

    def __init__(self):
        self.system = get_system_info()
        self.headers = {}

    def make_response(self):
        resp = {
            "OS": self.system.OS_NAME,
            "Host": self.system.HOST_NAME,
            "user": self.system.USER_NAME
        }
        return json.dumps(resp)


