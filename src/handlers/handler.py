import json
from typing import Dict


def hello(event: Dict[str, str], context: Dict[str, str]) -> Dict[str, object]:
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
