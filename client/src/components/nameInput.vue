<template>
  <v-card v-if="!userName" class="pa-6">
    <p class="font-weight-black">What's your name?</p>
    <v-text-field
      placeholder="Name"
      label="Name"
      :value="userNameInput"
      @input="updateName"
      @change="setName"
    ></v-text-field>
  </v-card>
</template>

<script>
import { mapState } from "vuex";

import { CREATE_USER, create_user } from "../../message-types.js";
export default {
  data: function() {
    return {};
  },
  computed: {
    ...mapState({
      userNameInput: state => state.userNameInput,
      userName: state => state.userName
    })
  },
  methods: {
    updateName(name) {
      this.$store.commit("updateName", name);
    },
    setName() {
      if (this.userNameInput !== "") {
        this.$socket.client.emit(CREATE_USER, create_user(this.userNameInput));
      }
    }
  }
};
</script>
<style>
</style>
