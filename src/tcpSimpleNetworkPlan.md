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

