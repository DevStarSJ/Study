'use strict';

function get(userId) {
  return {
    body: { id: userId, name: "test" }
  };
}

function post(userId, header, body) {
  return {
    body: { id: userId, header: header, body: body }
  };
}

const routeMap = {
  '/test': {
    'GET': (event, context) => {
      const userId = event.queryStringParameters.id;
      return get(userId);
    },
    'POST': (event, context) => {
      const userId = event.queryStringParameters.id;
      const body = JSON.stringify(event.body);
      const header =  event.headers;
      return post(userId, header, body);
    }
  }
};

function router(event, context) {
  const controller = routeMap[event.path][event.httpMethod];

  if(!controller) {
    return {
      body: { Error: "Invalid Path" }
    };
  }

  return controller(event, context);
}

exports.handler = (event, context, callback) => {
   let result = router(event, context);
   callback(null, {body:JSON.stringify(result)});
}