var app = require('express')();
var http = require('http').Server(app);

var port = process.env.PORT || 8001;

var server = app.listen( port, function(){
  console.log(`server running on port ${ port }`);
});

var io = require('socket.io').listen(server);
var directory = [];
io.on('connection', function(socket){
  var username;
  var pk;
  var directoryId;
  var directoryObj;
  socket.on('profile', function(msg){
    //console.log('user ' + msg.username + ' has signed in');
    //io.emit('chat-message', msg);
  });

  socket.on('chat-message', function(msg){
    console.log('message: ' + msg.msg);
    //var chatMsg = ''
    io.emit('chat-message', msg);
  });

  socket.on('disconnect', function() {
      console.log('User[' + pk +'] ' + username + ' has disconnected');
      //var i = allClients.indexOf(socket);
      //allClients.splice(i, 1);
      //let obj = directory.find(x => x.name == username);
      let index = directory.indexOf(directoryObj);
      console.log(index);
      directory.splice(index, 1);
      printDirectory();
   });
   pk = socket.handshake.query.pk;
   username = socket.handshake.query.username;
   console.log('User[' + socket.handshake.query.pk +'] ' +socket.handshake.query.username + ' has logged in');
   //console.log(socket.id)
   directoryObj = {clientId:socket.id, username:username, id:pk};
   directory.push(directoryObj);
   console.log(directory.length);
   printDirectory();
});

function printDirectory() {
  for(x in directory) {
    console.log(directory[x].username);
  }
}
