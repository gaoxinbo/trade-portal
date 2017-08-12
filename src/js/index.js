//import Vue from "Vue";
import Vue from 'vue/dist/vue.js'

import App from './components/banner.vue'
import positionApp from "./components/homepage/PositionTable.vue"
import buildVersionApp from "./components/BuildVersion.vue"

var banner = new Vue({
  el: '#banner',
  render: function(createElement) {
    return createElement(App);
  }
});


var p = new Vue({
  el: '#vue-position',
  render: function(createElement) {
    return createElement(positionApp);
  }
});

new Vue({
  el : '#buildVersion',
  render: function(createElement) {
    return createElement(buildVersionApp);
  }
});


