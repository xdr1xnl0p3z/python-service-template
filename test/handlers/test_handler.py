from typing import Dict

from src.handlers import handler

STATUS_OK = 200


def test_hello():
    response: Dict[str, object] = handler.hello({}, {})

    assert response['statusCode'] == STATUS_OK
