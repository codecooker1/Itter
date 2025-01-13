<template>
  <aside class="userbar">
    <form class="max-w-sm mx-auto" @submit.prevent="createPost" method="post">
      <label for="message" class="block mb-2 text-sm font-medium text-white">What's on your mind?</label>
      <textarea id="message " rows="4" v-model="content"
        class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
        placeholder="What's on your mind..." name="message" required></textarea>
      <button type="submit" name="submit"> Create Post </button>
    </form>
    <p v-if="error">{{ error }}</p>
    <div class="flex-spacer"></div>
  </aside>
</template> 

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/store/auth.js';

const content = ref('')
const error = ref(null)
const authStore = useAuthStore()

async function createPost() {
  const response = await fetch('https://itter.pythonanywhere.com/api/create/post', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.csrfToken
    },
    body: JSON.stringify({
      content: content.value
    }),
    
  })

  const data = await response.json()  

  if (data.error) {
    console.log(data.error)
    error.value = data.error
  }else {
    console.log('success')
    error.value = null
    content.value = ''
    
  }
}
</script>

<style>
.userbar {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
  overflow: hidden;
  width: inherit;
  position: fixed;
}

.flex-spacer {
  flex: 1 1 auto;
}
</style>
