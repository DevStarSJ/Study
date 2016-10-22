var http = require('http');

var options = {
    host: 'app1.kab.co.kr',
    path: '/zigbang/zigbang.json?BJD_CODE=2650010100&BUNJI=979&HO=72',
    port: '8082',
    method: 'GET'
};

function readJSONResponse(response) {
    var responseData = '';
    response.on('data', function (chunk) {
        responseData += chunk;
    });
    response.on('end', function () {
        var dataObj = JSON.parse(responseData);
        console.log("Raw Response: " +responseData);
        console.log("Message: " + dataObj.message);
        console.log("Question: " + dataObj.question);
    });
}
var req = http.request(options, readJSONResponse);
//req.write('{"name":"Bilbo", "occupation":"Burglar"}');
req.end();