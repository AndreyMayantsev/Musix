from musix_app.core.system_info import get_system_info


class SystemService:
    # About system

    def __init__(self):
        self.system = get_system_info()
        self.headers = {}

    def make_response(self):
        resp = {
            "OS": self.system.OS_NAME,
            "Host": self.system.HOST_NAME,
            "user": self.system.USER_NAME,
            "processor": self.system.PROCESSOR_INFO
        }
        return {"data": resp}
