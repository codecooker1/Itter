<template>
  <img :src="props.picUrl" width="42" height="42" alt="profile_pic" />
</template>

<script setup>
const props = defineProps(['picUrl'])
</script>

<style scoped>
img {
  border-radius: 50%;
  height: 42px;
  width: 42px;
}
</style>
