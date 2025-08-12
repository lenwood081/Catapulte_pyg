# Plan for simple tcp server network

## Connections

Host creates server
Host client connects to server
opponent client connects to server

Connection is TCP

## Server

Server simulates whole game
Sends updated pixel colors to clients
Sends avalible actions to clients
Recieves commands from clients

## Client

Recieves colors from server
updates the pixels needed and displays to user
Has a actions it can preform, sends results to server

## Notes

### Pros

    - not much information being sent back and forth (only colors)
    - client side is very lightweight

### Cons

    - server side is very heavy, doing all the computations
    - Actions must first reach the server, affect it, before
      being sent back to the client (potentual lag)
    - options for actions must first be verifyed by the server,
        for example highlighting where movement it possible, or
        building is possible

## Example

* Server starts

* Both clients connect to 

    - if either client disconnects, inform other client, and close all connections, stop game

* Server sends initiation message to both clients

    - SOM, SOF start screen, any other information needed to start the game, EOF

* Both clients Recieves SOM and displays the start screen

* Server sends updated pixels to both clients

    - SOF, (rgb, (x, y)), EOF

* Both clients recieve the updated pixels and make changes to their display

--> TODO, actions from client

* Server closes connections on game end

    - SOF, EOF, EOM

** Special case, if one client disconnects

    - Server sends SOF, client disconnected, EOF, EOM


