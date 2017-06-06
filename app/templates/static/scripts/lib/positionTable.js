define(function (require) {

    var $ = require('jquery');
    var Vue = require('Vue');


    return {
        renderPositionTable : function() {
            return new Vue({
                delimiters: ['[[', ']]'],
                el: '#position',
                data: {
                        'header' : [
                            'Symbol',
                            'Position',
                            'Average Cost',
                            'Currency'
                        ],
                        'content' : []
                },

                mounted: function() {
                    var self = this;

                    $.ajax({
                        url: '/position',
                        method: 'GET',
                        success: function (data) {
                            self.content = data;
                        }   
                    });
                }

            })
        },
        
    };
    


});
