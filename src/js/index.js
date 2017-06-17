//import Vue from "Vue";
import Vue from 'vue/dist/vue.js'

import App from './components/banner.vue'
import positionApp from "./components/PositionTable.vue"
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



// var app = new Vue({
//                 el: '#position',
//                 data: {
//                         'header' : [
//                             'Symbol',
//                             'Position',
//                             'Average Cost',
//                             'LastClosePrice',
//                             'LastTradeDate',
//                             'Profit',
//                             'Currency',

//                         ],
//                         'content' : []
//                 },

//                 mounted: function() {
//                     var self = this;

//                     $.ajax({
//                         url: 'http://192.168.1.80:8000/position',
//                         method: 'GET',
//                         jsonp: "callback",
//                         dataType: "jsonp",
//                         success: function (data) {
//                             self.content = data;
//                         }   
//                     });
//                 }

//             });
