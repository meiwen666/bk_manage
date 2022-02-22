import { createApp } from 'vue';
// import Vue from 'vue';
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import App from './App.vue';
//import router from './router';
import store from './store';

// if (process.env.NODE_ENV == 'development') {
//     Vue.config.devtools = true;
// } else {
//     Vue.config.devtools = false;
// }


let Vue = createApp(App)
if (process.env.NODE_ENV == 'development') {
    Vue.config.devtools = true;
} else {
    Vue.config.devtools = false;
}
Vue.use(ElementPlus).use(store).mount('#app');