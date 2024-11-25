<!-- eslint-disable no-unused-vars -->
<template>
  <LoaderView v-if="isLoading" />
  <RouterView v-else />
</template>

<script setup>
//import NavbarView from './components/NavbarView.vue'

import { ref, onMounted, watchEffect } from 'vue'
import { useAuthStore } from '@/store/auth.js'
import { useRouter } from 'vue-router'
import LoaderView from '@/components/LoaderView.vue'

const authStore = useAuthStore()
const router = useRouter()
const isLoading = ref(null)

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

// Watch for route changes and set loading state
watchEffect(() => {
  isLoading.value = true // Set loading to true before route change completes
  router.isReady().then(() => {
    isLoading.value = false // Set loading to false after route change completes
  })
})
</script>

<style></style>
