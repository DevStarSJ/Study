import controllers.test.get
import controllers.test.post

route_map = {
    '/test': {
        'GET': controllers.test.get.handler,
        'POST': controllers.test.post.handler
    }
};

def router(event):
    controller = route_map[event['path']][event['httpMethod']];
    
    if not controller:
        return { 'body': { 'Error': "Invalid Path" } }
    
    return controller(event);