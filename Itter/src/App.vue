<!-- eslint-disable no-unused-vars -->
<template>
  <RouterView></RouterView>
</template>

<script setup>
//import NavbarView from './components/NavbarView.vue'

import {  onMounted } from 'vue'
import { useAuthStore } from '@/store/auth.js'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

// eslint-disable-next-line no-unused-vars
const logout = async () => {
  try {
    await authStore.logout(router)
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  await authStore.fetchUser()
})
</script>

<style></style>
