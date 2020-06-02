# client

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn run serve
```

### Compiles and minifies for production
```
yarn run build
```

### Run your tests
```
yarn run test
```

### Lints and fixes files
```
yarn run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


What I hope to integrate and design patterns to achieve
- Using VueX to manage state
- Using Constants for mutation types
- Mapping mutations and getters in components
- Handle all socket communication in VueX actions.
- Use VueX and VueSocketIO to handle messages from the server in a centralized store.


I need to first determine the behaviors I want to implement and think about the messages to be sent.

MVP (ignore login. Make it work for just our group of friends)
- User can set their name.
  - send CREATE_USER message to server. Get userID back from server
- User can create a room (give the room a name)
  - send CREATE_ROOM message to server. Server emits FETCH_ROOMS message to all clients. Get roomID back from server.
- User can select a room to join (loaded on dashboard)
  - send JOIN_ROOM message to server. Server emits FETCH_ROOM message to all clients in the room.
- User can press 'start' when in a room to start the game.
  - send START_GAME to server. Server emits START_GAME response to all clients in the room. 
- User can submit answers to a question.
  - send SUBMIT_ANSWER message to server. Server responds with SUBMIT_ANSWER message. If answer is correct, send NEXT_QUESTION message to all connected clients.
  -
Messages sent from client to server:

Create abstraction to generate messages based on their types.
{
    type: "socket channel / type of message?",
    payload: {
        # anything we need to send over.
    }
}

CREATE_USER: 
- type: "create_user"
- payload: {name: "user name"}

CREATE_ROOM
- type: "create_room"
- payload: {roomName: "room name", userID: "user id who is creating the room"}

JOIN_ROOM
- type: "join_room"
- payload: {roomId, userID}

FETCH_ROOM
- type: "fetch_room"
- payload: {roomId}
FETCH_ROOMS
- type: "fetch_rooms"
- payload: {}

START_GAME
- type: 'start_game'
- payload: {roomId}

SUBMIT_ANSWER
- type: "submit_answer"
- payload: {roomId, userId, answer}


Messages sent from server to client: should these match types from server to client?

{
    type: "socket channel / type of message",
    status: Int (returns -1 on error. 0 on success of action?)
    errorMessage: message if there is a -1.
    payload: {
        # anything we need to send over.
    }

}

Server responses on success
CREATE_USER: 
- type: "create_user"
- payload: {userId}

CREATE_ROOM
- type: "create_room"
- payload: {roomId}

JOIN_ROOM
- type: "join_room"
- payload: {}

FETCH_ROOMS
- type: "fetch_rooms"
- payload: {rooms: [array of rooms]}

START_GAME
- type: 'start_game'
- payload: {question: "string to display question"}

SUBMIT_ANSWER
- type: "submit_answer"
- payload: {correct: 1 or 0 for if answer was correct or not}


Task: setup VueX and socketIO!
