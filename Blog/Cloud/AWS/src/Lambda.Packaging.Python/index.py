#import json

def get(event):
    user_id = event['queryStringParameters']['id']
    return { 'body': { 'id': user_id, 'name': "test" } }

def post(event):
    user_id = event['queryStringParameters']['id']
    body = event['body']
    header = event['headers']
    return { 'body': { 'id': user_id, 'header': header, 'body': body } }

route_map = {
    '/test': {
        'GET': get,
        'POST': post
    }
};

def router(event):
    controller = route_map[event['path']][event['httpMethod']];
    
    if not controller:
        return { 'body': { 'Error': "Invalid Path" } }
    
    return controller(event);

def handler(event, context):
    result = router(event);
    return { 'body' : str(result) }
    #return { 'body' : json.dumps(result) }