var express = require('express');
var app = express();

app.get('/', function(req, res){
    res.send('Hello home app');
});

app.get('/login', function(req, res){
    res.send('Login please.');
});

app.listen(3000, function() {
    console.log('Connected 3000 port!');
});