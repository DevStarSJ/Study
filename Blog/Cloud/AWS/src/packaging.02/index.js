'use strict';

const router = require('./router');

exports.handler = (event, context, callback) => {
   let result = router(event, context);
   callback(null, {body:JSON.stringify(result)});
   //callback(null, {body:JSON.stringify(event)});
}