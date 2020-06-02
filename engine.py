import random
import json
import uuid


class Engine:
    """
    Holds the list of rooms?
    """

    def __init__(self):
        """
        Each room has:
        - users dict: id -> {USER OBJECT}
        - questions array: (question, answer)
        - current idx

        """
        self.rooms = {}
        self.users = {}

    def getState(self, roomId, data="users"):
        if data == "users":
            room = {roomId: self.rooms[roomId]}
            return json.dumps(room)
        elif data == "rooms":
            rooms = {}
            for key in self.rooms:
                rooms[key] = key
            return json.dumps(rooms)

    def createRoom(self):
        """
        Create a room and return the room_id
        """
        id = uuid.uuid1().int
        while id in self.rooms:
            id = uuid.uuid1()

        self.rooms[id] = {"users": {}}
        self.generateQuestion(id)
        return id

    def createUser(self, userName):
        userID = uuid.uuid4().int
        self.users[userID] = userName
        return userID

    def generateQuestion(self, roomId):
        """
        generate questions for the game
        """
        operators = "+-*"
        operator = operators[random.randint(0, len(operators) - 1)]
        val1, val2 = (random.randint(1, 100), random.randint(1, 100))
        if operator == "*":
            val1, val2 = (random.randint(1, 10), random.randint(1, 10))

        result = None
        if operator == "+":
            result = val1 + val2
        elif operator == "-":
            result = val1 - val2
        else:
            result = val1 * val2
        self.rooms[roomId]["answer"] = result
        self.rooms[roomId]["question"] = (val1, operator, val2, result)

    def join_room(self, roomid, userid):
        userName = self.users[userid]
        users = self.rooms[roomid]["users"]
        if userid in users:
            return
        users[userid] = {"name": userName, "score": 0}
        return 0

    def submit_answer(self, userId, roomId, answer):
        """
        if return 0, then answer was correct
        """
        answer = int(answer)
        print(self.rooms)
        room = self.rooms[roomId]
        if answer == room["answer"]:
            rooms["users"][userId]["score"] += 1
            return 0
        else:
            return -1
        # generate new question
        self.generateQuestion(self, roomId)
