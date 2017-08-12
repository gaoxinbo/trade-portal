<template >
    <div>
        <h1> Overview </h1>
        <h2> Position </h2>
        <position></position>
    </div>
</template>


<script>

import positionApp from "./PositionTable.vue";

export default {
    components : {
        position : positionApp
    }
};

</script>