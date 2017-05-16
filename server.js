var app = require('express')();
var http = require('http').Server(app);

var port = process.env.PORT || 8001;

var server = app.listen( port, function(){
  console.log(`server running on port ${ port }`);
});

var io = require('socket.io').listen(server);

io.on('connection', function(socket){
  console.log('a user connected');

  socket.on('chat-message', function(msg){
    console.log('message: ' + msg);
    io.emit('chat-message', msg);
  });
});
