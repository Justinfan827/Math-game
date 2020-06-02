import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import VueSocketIOExt from "vue-socket.io-extended";
import io from "socket.io-client";
import VueMaterial from "vue-material";
import "vue-material/dist/vue-material.min.css";

import { store } from "./store";
import App from "./App.vue";

Vue.use(VueMaterial);
Vue.use(Vuetify);

Vue.use(VueSocketIOExt, io("http://localhost:5000"), { store });
Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
  vuetify: new Vuetify(),

  store,
}).$mount("#app");
