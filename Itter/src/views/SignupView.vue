<template>
    <h1>{{ data }}</h1>
</template>


<script setup>
let data = await fetch('http://localhost:8000/api/', {mode:'no-cors'})
console.log('code reached')
console.log(data)
</script>
