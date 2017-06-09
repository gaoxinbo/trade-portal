<template>
    <div id="banner">
        <h1>{{ text }}</h1>
    </div>
</template>

<script>
    module.exports = {
        data : function() {
            return {
                text : "Trading Portal"
            }
        }
    }
</script>

<style scoped>
h1 {
    color : #FFF;
    margin-left : 100px;
};

#banner {
    background-color:#563d7c;
    padding-bottom:60px;
    padding-top:60px;
    margin-top:20px;
    margin-bottom:20px;
}
</style>


