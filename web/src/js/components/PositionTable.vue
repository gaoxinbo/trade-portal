<template>
    <div id="position">
        <table class="table">
            <tr>
                <th v-for="h in header"> 
                        {{ h }}
                </th>
            </tr>
            <tr v-for="contract in content">
                <td>{{ contract.symbol }}  </td>
                <td>{{ contract.position }}</td>
                <td>{{ contract.avgCost }}</td>
                <td>{{ contract.lastClosePrice }}</td>
                <td>{{ contract.lastTradingDate }}</td>
                <td>{{ contract.profit }}</td>
                <td>{{ contract.currency }}</td>
            </tr>
        </table>
    </div>
</template>


<script>
var $ = require("jquery");

module.exports = {
    data : function() {
        return {
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
        }
    },
    mounted: function() {
        var self = this;

        $.ajax({
            url: 'http://192.168.1.80:8000/dataservice/position',
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


<style scoped>
tr {
    height : 39px;
}
td {
    padding : 8px;

}
table {
    border : 1;
}
</style>
