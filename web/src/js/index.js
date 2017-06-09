//import Vue from "Vue";
import Vue from 'vue/dist/vue.js'
import $ from "jquery";
import App from './components/banner.vue'

var banner = new Vue({
  el: '#banner',
  render: function(createElement) {
    return createElement(App);
  }
})

var app = new Vue({
                delimiters: ['[[', ']]'],
                el: '#position',
                data: {
                        'header' : [
                            'Symbol',
                            'Position',
                            'Average Cost',
                            'LastClosePrice',
                            'LastTradeDate',
                            'Profit',
                            'Currency',

                        ],
                        'content' : []
                },

                mounted: function() {
                    var self = this;

                    $.ajax({
                        url: 'http://192.168.1.80:8000/position',
                        method: 'GET',
                        jsonp: "callback",
                        dataType: "jsonp",
                        success: function (data) {
                            self.content = data;
                        }   
                    });
                }

            });
