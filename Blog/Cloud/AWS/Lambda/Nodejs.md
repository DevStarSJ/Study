# AWS Labmda using Node.JS

## Handler

- index.js

```JavaScript
exports.myHandler = function(event, context, callback) {
   ...
   // The callback parameter is optional
   // Use callback() and return information to the caller.  
}
```

## Handler to Router for API

- index.js

```JavaScript
const router = require('./router');

exports.myHandler = function(event, context, callback) {
   ...
   router(event, context).then(results => {
     callback(null, results);
   }).catch(err => {
     callback(err);
   });
}
```

- router.js

```JavaScript
const Promise = require('bluebird');

const routeMap = {
  '/test/{userId}': {
    'GET': (event, context) => {
      const userId = event.params.path.userId;
      return require('./controllers/test/get')(userId);
    },
    'POST': (event, context) => {
      const userId = event.params.path.userId;
      const body = JSON.parse(event.body);
      const header = event.params.header;
      return require('./controllers/test/post')(userId, header, body);
    }
  }
};

module.exports = (event, context) => {
  const controller = routeMap[event.context.resourcePath][event.context.httpMethod];

  if(!controller) {
    return Promise.reject('');
  }

  return controller(event, context);
};
```

## API Functions

- controllers/test/get.js

```JavaScript
const Promise = require('bluebird');

module.exports = (userId) => {
  return Promise.resolve({
    body: JSON.stringify({ id: userId, name: "test" })
  });
};
```

- controllers/test/post.js

```JavaScript
const Promise = require('bluebird');
module.exports = (userId, header, body) => {
  return Promise.resolve({
    body: JSON.stringify({ id: userId, header: header, body: body })
  });
};
```
