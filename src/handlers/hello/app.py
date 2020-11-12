import json
from typing import Dict


def say_hello(event: Dict[str, str]) -> Dict[str, str]:
    body = {
        'message': 'Go Serverless v1.0! Your function executed successfully!',
        'input': event,
    }

    return {'statusCode': 200, 'body': json.dumps(body)}
