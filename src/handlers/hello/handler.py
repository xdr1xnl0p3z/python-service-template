from typing import Dict

from src.handlers.hello.app import say_hello


def handler(
    event: Dict[str, str],
    context: Dict[str, str],
) -> Dict[str, object]:
    return say_hello()
