import json
import requests

from router import router

def handler(event, context):
    result = router(event);

    URL = 'http://www.tistory.com'
    response = requests.get(URL)

    result['request_data'] = response.text

    return { 'body' : json.dumps(result) }