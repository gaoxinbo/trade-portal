<template>
    <div>
        <p>
            backend:
            {{content.buildDate}}
            {{content.buildVersion}}
            @ {{content.buildHost}} 
        </p>
    </div>

</template>


<script>
    var $ = require("jquery");


    module.exports = {
        data : function() {
            return {
                "content" : {}
            }
        },

        mounted : function() {
            var self = this;

            $.ajax({
                url: 'http://192.168.1.80:8000/dataservice/build',
                method: 'GET',
                jsonp: "callback",
                dataType: "jsonp",
                success: function (data) {
                    self.content = data;
                }   
            });
        }


    }
</script>
