var app = require('express')();
var http = require('http').Server(app);

var port = process.env.PORT || 8001;

var server = app.listen( port, function(){
  console.log(`server running on port ${ port }`);
});

var io = require('socket.io').listen(server);

io.on('connection', function(socket){
  var username;
  var pk
  socket.on('profile', function(msg){
    //console.log('user ' + msg.username + ' has signed in');
    //io.emit('chat-message', msg);
  });

  socket.on('chat-message', function(msg){
    console.log('message: ' + msg);
    io.emit('chat-message', msg);
  });

  socket.on('disconnect', function() {
      console.log('User[' + pk +'] ' + username + ' has disconnected');
      //var i = allClients.indexOf(socket);
      //allClients.splice(i, 1);
   });
   pk = socket.handshake.query.pk;
   username = socket.handshake.query.username;
   console.log('User[' + socket.handshake.query.pk +'] ' +socket.handshake.query.username + ' has logged in');
});
