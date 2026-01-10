import datetime
import json
from enum import Enum


class ResponseType(Enum):
    OK = "success"
    SystemError = "error"
    NetworkError = "error"
    UndefinedError = "error"


def compose_response(type: ResponseType, data):
    response = {
        "type": type.value,
        "timestamp": datetime.datetime.now(),
        "data": json.dumps(data)
    }
    return response
