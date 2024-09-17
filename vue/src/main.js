import axios from "axios";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

import { createApp } from "vue";
import App from "./App.vue";

createApp(App).mount("#app");
