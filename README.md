# Math-game
Simple math game to determine who is better at math.

Current stage: 
1. Shooting for MVP: Be able to connect to a single room and race each other to finish 20 quick-math calculations

Web socket messages:
- Client to server:
  - create-room(user-id): create a room for people to join
    - returns room-id
  - join-room(user-id): join a room given given user-id
     - broadcast to other users in room someone has joined
  - leave-room(room-id, user-id): leave a room
  - delete-room(room-id): delete a room given a user-id
  - submit-answer(answer, room-id): submit-answer to room
  - broadcast-correct-answer(answer, room-id): broadcast the right answer to all users

Backend: 

- Flask web socket-io.
- Data structures:
  - Active room dictionary -> room-id to set of user-ids, question and answer tuple!
  - Abstract all logic away to a game object? 1 game object per room or 1 engine holding all the games?



