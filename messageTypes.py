import json
from enum import Enum


class MessageTypes(Enum):
    CREATE_USER = "create_user"


class BaseMessage:
    def __init__(self):
        self.msg = {"type": None, "payload": {}}

    def getMsg(self):
        return self.msg

    def __str__(self):
        return json.dumps(self.msg, indent=1)


class CreateUserMessage(BaseMessage):
    def __init__(self):
        super().__init__()
        self.msg["type"] = MessageTypes.CREATE_USER.value

    def genPayload(self, userName, userID):
        print("ere")
        payload = {"userName": userName, "userID": userID}
        self.msg["payload"] = payload
        return self
