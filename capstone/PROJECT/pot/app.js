var express  = require('express');

var app      = express();

//var app      = require('express')();

 

//var http     = require('http');

//var server   = http.Server(app);

var http     = require('http').Server(app);

 

//var socketio = require('socket.io');

//var io       = socketio(server);

var io       = require('socket.io')(http);

 

const path = require('path');

 

var SerialPort = require('serialport').SerialPort;

var ReadlineParser = require('@serialport/parser-readline').ReadlineParser;

var parsers    = SerialPort.parsers;

var sp = new SerialPort( {

  path:'COM3',

  baudRate: 115200

});

var parser     = sp.pipe(new ReadlineParser({

  delimiter: '\r\n'

}));

 

 

 

var port = 3000;

 

sp.pipe(parser);

 

sp.on('open', () => console.log('Port open'));

 

parser.on('data', function(data)

{

	var rcv = data.toString();

	if(rcv.substring(0,3) == "led"){

		if(rcv.substring(3,4) == "1")	ledStatus = "on";

		else							ledStatus = "off";

		io.emit('led', ledStatus);

		console.log('led status: ' + ledStatus);

	}

	else if(rcv.substring(0,3) == "abc"){

		adcValue = rcv.substring(3);

		io.emit('adc', adcValue);

		console.log('adc value:'+adcValue);

	}

});

 

app.get('/led_on',function(req,res)

{

	sp.write('led1\n\r', function(err){

		if (err) {

            return console.log('Error on write: ', err.message);

        }

        console.log('send: led on');

		res.writeHead(200, {'Content-Type': 'text/plain'});

		res.end('LED ON\n');

	});

});

 

app.get('/led_off',function(req,res)

{

	sp.write('led0\n\r', function(err){

		if (err) {

            return console.log('Error on write: ', err.message);

        }

        console.log('send: led off');

		res.writeHead(200, {'Content-Type': 'text/plain'});

		res.end('LED OFF\n');

	}); 

});

 

app.use(express.static(__dirname + '/public'));

 

http.listen(port, function() {  // server.listen(port, function() {

    console.log('listening on *:' + port);

});
