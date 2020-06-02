export const CREATE_USER = "create_user";
export const CREATE_ROOM = "create_room";
export const JOIN_ROOM = "join_room";
export const FETCH_ROOMS = "fetch_rooms";
export const START_GAME = "start_game";
export const SUBMIT_ANSWER = "submit_answer";

export const create_user = (userName) => ({
  type: CREATE_USER,
  payload: {
    userName,
  },
});

export const create_room = (userID, roomName) => ({
  type: CREATE_ROOM,
  payload: {
    userID,
    roomName,
  },
});
