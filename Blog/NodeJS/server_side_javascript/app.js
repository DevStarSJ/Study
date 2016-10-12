var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.locals.pretty = true;

app.set('view engine', 'jade');
app.set('views', './views');

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:false}));

app.get('/', function(req, res){
    res.send('Hello home app');
});

app.get('/template', function(req, res) {
    res.render('temp', {time:Date(), _title:'Jade'});
});

app.get('/route', function(req, res) {
    res.send('Hello Router, <img src ="/test.jpg">');
});

app.get('/dynamic', function(req, res) {
    var time = Date();
    var lis = '';
    for (var i = 0; i < 5; i++) {
        lis += '<li>coding</li>';
    }
    var output = ` 
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>NodeJS</title>
        </head>
        <body>
            Hello Dynamic !
            <ul>
                ${lis}
            </ul>
            ${time}
        </body>
        </html>`;
    res.send(output);
});

app.get('/login', function(req, res){
    res.send('Login please.');
});

app.get('/topic',function(req, res) {
    var topics = [
        'Javascript is...',
        'Nodejs is...',
        'Express is...'
    ];
    var str = `
        <a href='/topic?id=0'>JavaScirpt</a><br>
        <a href='/topic?id=1'>Nodejs</a><br>
        <a href='/topic?id=2'>Express</a><br><br>`;
    var output = str + topics[req.query.id];
    res.send(output);
});

app.get('/topic/:id',function(req, res) {
    var topics = [
        'Javascript is...',
        'Nodejs is...',
        'Express is...'
    ];
    var str = `
        <a href='/topic?id=0'>JavaScirpt</a><br>
        <a href='/topic?id=1'>Nodejs</a><br>
        <a href='/topic?id=2'>Express</a><br><br>`;
    var output = str + topics[req.params.id];
    res.send(output);
});

app.get('/param/:module_id/:topic_id', function(req, res){
    res.json(req.params);
});

app.get('/form', function(req, res) {
    res.render('form');
});

app.get('/form_receiver', function (req, res) {
    var title = req.query.title;
    var description = req.query.description;
    res.send(title + ',' + description);
});

app.post('/form_receiver', function(req, res) {
    var title = req.body.title;
    var description = req.body.description;
    res.send(title + ',' + description);
});

app.listen(3000, function() {
    console.log('Connected 3000 port!');
});