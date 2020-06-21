<template>
    <div class="hello">
        <h1> My first component using Vue.js, this is so cool. </h1>
        <p>
            <b>Message from Lucas:</b> {{ message }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'Tasks',
    props: {
        message: String
    } 
}
</script>

<style scoped>
b {
    color: #42b983;
}
</style>