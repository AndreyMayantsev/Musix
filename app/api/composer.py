import datetime
from enum import Enum


class ResponseType(Enum):
    OK = "success"
    SystemError = "error"
    NetworkError = "error"
    UndefinedError = "error"


def compose_response(resp_type: ResponseType, data):
    response = {
        "type": resp_type.value,
        "timestamp": datetime.datetime.now(),
        "data": data
    }
    return response
