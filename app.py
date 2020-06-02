from flask import Flask, render_template
from flask_cors import CORS
import sys
from flask_socketio import SocketIO, join_room, emit, send
from engine import Engine
from messageTypes import CreateUserMessage

# initialize Flask
app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")
engine = Engine()


@app.route("/")
def index():
    """Serve the index HTML"""
    return render_template("index.html")


@socketio.on("connect")
def connect():
    print(f"connected", file=sys.stderr)
    send("HELLO")
    emit("connect", "hello")


@socketio.on("create_user")
def create_user(data):
    global engine
    payload = data["payload"]
    userName = payload["userName"]
    userID = engine.createUser(userName)
    msg = CreateUserMessage().genPayload(userName=userName, userID=userID)
    print(f"CreateUser response {msg}")
    emit("create_user", msg.getMsg())


@socketio.on("create_room")
def on_create(data):
    global engine
    user = data["user"]
    userID = engine.createUser(user)
    roomID = engine.createRoom()
    engine.join_room(roomID, userID)
    join_room(roomID)
    # let client know they've joined the room
    emit("create_room", {"roomState": engine.getState(roomID)}, room=roomID)


@socketio.on("join_room")
def on_join(data):
    print(f"JOINING ROOM", file=sys.stderr)
    global engine
    roomID = data["room"]
    userID = data["user"]
    engine.join_room(roomID, userID)
    join_room(roomID)
    send(f"{userID} has joined the room", room=roomID)


@socketio.on("fetch_rooms")
def on_fetch():
    emit("fetch_rooms", {"rooms": engine.getState(None, "rooms")})


@socketio.on("submit_answer")
def on_submit(data):
    global engine
    answer = data["answer"]
    userID = data["userID"]
    roomID = int(data["roomID"])
    status = engine.submit_answer(userID, roomID, answer)
    emit("submit_answer", {"status": status, "room": engine.getState(roomID)})


if __name__ == "__main__":
    socketio.run(app, debug=True)
