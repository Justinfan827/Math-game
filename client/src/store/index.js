import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export const store = new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
    }),
  ],
  state: {
    connected: false,
    userID: "",
    userNameInput: "",
    userName: "",
    roomID: "",
  },
  getters: {},
  mutations: {
    updateName(state, name) {
      console.log("setting name: ", name);
      state.userNameInput = name;
    },
    setName(state, payload) {
      console.log("mutation setName");
      console.log(payload);
      state.userName = payload.userName;
      state.userID = payload.userID;
    },
  },

  actions: {
    socket_connect(state) {
      state.connected = true;
    },
    socket_createUser({ commit }, { payload }) {
      console.log("action: create_user");
      commit("setName", payload);
    },
    socket_createRoom({ commit }, { payload }) {
      console.log(payload, commit);
    },
  },
});
