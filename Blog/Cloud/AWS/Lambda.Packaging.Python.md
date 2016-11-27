# Lambda Python Packaging

### Step 1

#### index.js
```Python
import json

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
    return { 'body' : json.dumps(result) }
```


### Step 2

#### index.js
```Python
import json
from router import router

def handler(event, context):
    result = router(event);
    return { 'body' : json.dumps(result) }
```

#### router.js
```Python
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
```


### Step 3

#### index.js
```Python
import json
from router import router

def handler(event, context):
    result = router(event);
    return { 'body' : json.dumps(result) }
```

#### router.js

```Python
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
```
#### controllers/__init__.py

#### controllers/test/__init__.py

#### controllers/test/post.py

```Python
def handler(event):
    user_id = event['queryStringParameters']['id']
    body = event['body']
    header = event['headers']
    return { 'body': { 'id': user_id, 'header': header, 'body': body } }
```

#### controllers/test/get.py

```Python
def handler(event):
    user_id = event['queryStringParameters']['id']
    return { 'body': { 'id': user_id, 'name': "test" } }
```

### Step 4