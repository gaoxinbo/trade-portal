//import Vue from "Vue";
import Vue from 'vue/dist/vue.js'
import $ from "jquery";


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
                        url: '/api/position',
                        method: 'GET',
                        jsonp: "callback",
                        dataType: "jsonp",
                        success: function (data) {
                            self.content = data;
                        }   
                    });
                }

            });