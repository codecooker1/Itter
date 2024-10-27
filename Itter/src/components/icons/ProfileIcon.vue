<template>
        <img :src="props.picUrl" alt="profile_pic">
</template>

<script setup>
// import {ref} from 'vue'

// const url = ref('https://jzydvbxwyynlezjnqbbd.supabase.co/storage/v1/object/public/profilepics/1%20(1).png')

const props = defineProps(['picUrl'])

</script>

<style scoped>
img{
    border-radius: 50%;
}
</style>