'use strict';

const _ = require('lodash');

const routeMap = {
  '/test': {
    'GET': (event, context) => {
      const userId = _.get(event,'queryStringParameters.id');
      return require('./controllers/test/get')(userId);
    },
    'POST': (event, context) => {
      const userId = _.get(event,'queryStringParameters.id');
      const body = JSON.stringify(_.get(event,'body'));
      const header =  event.headers;
      return require('./controllers/test/post')(userId, header, body);
    }
  }
};

module.exports = (event, context) => {
  const controller = routeMap[event.path][event.httpMethod];

  if(!controller) {
    return {
      body: { Error: "Invalid Path" }
    };
  }

  return controller(event, context);
};