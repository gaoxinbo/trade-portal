require.config({
    paths:{
        'Vue' : 'https://unpkg.com/vue/dist/vue',
        "jquery": "https://ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min"
    }
});

require(['Vue', 'jquery'], function (Vue, $){
    // init position table
    var position = new Vue({
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

    });


});