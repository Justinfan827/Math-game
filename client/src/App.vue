<template>
  <v-app id="app">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="6">
            <NameInput v-if="!userName" />
            <RoomPage v-if="userName" />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import RoomPage from "./components/roomPage";
import NameInput from "./components/nameInput";
import { mapState } from "vuex";
export default {
  name: "App",

  computed: mapState({
    userName: state => state.userName
  }),
  components: {
    NameInput,
    RoomPage
  },

  data: () => ({
    //
  })
};
</script>
