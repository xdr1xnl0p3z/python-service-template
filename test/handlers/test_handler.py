from src.handlers import handler
from typing import Dict


def test_hello():
    response: Dict[str, object] = handler.hello({}, {})

    assert response["statusCode"] == 200
