<template>
  <v-card>
    <v-row align="center" justify="center">
      <v-col>
        <p class="text-center font-weight-bold">Hello {{ userName}}</p>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-list>
        <v-list-item>Item</v-list-item>
      </v-list>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="6" justify="center" align="center">
        <v-btn>Create Room</v-btn>
        <v-dialog max-width="600px">
          <v-btn flat></v-btn>
        </v-dialog>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "RoomPage",
  props: {
    msg: String
  },
  data() {
    return {};
  },

  computed: {
    ...mapState({
      userNameInput: state => state.userNameInput,
      userName: state => state.userName
    })
  },
  created() {},
  mounted() {},
  methods: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
.container {
  display: flex;
  justify-content: center;
  align-self: center;
}

.textField {
  width: 100px;
  background-color: grey;
  border: black;
  padding: 10px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.alert {
  color: red;
  font-size: 30px;
}
</style>
