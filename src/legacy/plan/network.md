## Networking Plan


### For two player

Have one player set up as ther server and the other as the client.
Connect via tcp or udp via a code. use simple local network for now
    - send special packet with code to all computers in network
    connect to one that responds

client player connects to server players game
server sends game state to client 
    - First use json, can compress if too slow
    - if still too slow send only tiles likly to be have been updated
client sends actions to server
    - possibly simluate actions locally and then validate with state recieved for
    smoother play

