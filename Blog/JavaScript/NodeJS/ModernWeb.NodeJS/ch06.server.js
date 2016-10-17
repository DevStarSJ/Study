/**
 * Created by seokjoonyun on 2016. 10. 7..
 */

var fs = require('fs');

var server = require('http').createServer(function (request, response) {
    // response.writeHead(200, {'Content-Type': 'text/html'});
    // response.end('<h1>Hello World ..!</h1>');

    fs.readFile('ch05.HTMLPage.html', function(error, data){
        response.writeHead(200, {
            'Content-Type': 'text/html',
            'Set-Cookie' : ['breakfast = toast' , 'dinner = chicken']
            });
        response.end('<H1>' +  request.headers.cookie + '</H1>');
        //response.end(data);
    });
});

server.listen(52273, function() {
    console.log('Server Running at http://127.0.0.1:52273');
});

server.on('request', function() {
    console.log('Request On')
});

server.on('connection', function() {
    console.log('Connection On')
});

server.on('close', function() {
    console.log('Close On')
});

// 서버 실행 후 10초 뒤 서버 종료
setInterval(function() {
    server.close();
}, 10000);
