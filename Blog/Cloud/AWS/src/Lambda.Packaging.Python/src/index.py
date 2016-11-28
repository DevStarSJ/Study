import json
import modules.requests

from router import router

def handler(event, context):
    
    packages = {}
    packages['requests'] = modules.requests
    
    result = router(packages, event);

    return { 'body' : json.dumps(result) }