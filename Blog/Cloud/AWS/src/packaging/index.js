'use strict';

const _ = require('lodash');

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
      const userId = _.get(event,'queryStringParameters.id');
      return get(userId);
    },
    'POST': (event, context) => {
      const userId = _.get(event,'queryStringParameters.id');
      const body = JSON.stringify(_.get(event,'body'));
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
   //callback(null, {body:JSON.stringify(event)});
}