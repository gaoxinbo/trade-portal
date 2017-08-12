import Vue from 'vue/dist/vue.js'
import VueRouter from 'vue-router'

import App from './components/banner.vue'
import buildVersionApp from "./components/BuildVersion.vue"
import overview from './components/overview/overview.vue'

Vue.use(VueRouter);

new Vue({
  el: '#banner',
  render: function(createElement) {
    return createElement(App);
  }
});

new Vue({
  el : '#buildVersion',
  render: function(createElement) {
    return createElement(buildVersionApp);
  }
});


const routes = [
  { path: '/', component: overview },
]

const router = new VueRouter({
  routes 
})

const app = new Vue({
  router
}).$mount('#app')
