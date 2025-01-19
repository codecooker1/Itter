<template>
  <div id="create-post-modal">
    <div class="create-post-background" @click="$emit('close')">
      <div class="create-post" @click.stop>
        <h2>Create a Post</h2>
        <form @submit.prevent="createPost">
          <label for="message" class="block mb-2 text-sm font-medium text-white"></label>
          <textarea v-model="postContent" placeholder="What's on your mind?" class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500" required></textarea>
          <button class="sbutton" type="submit" name="submit"> <IconLoading v-if="isPosting" /> Post</button>
        </form>
        <p v-if="error" class="text-red-500">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import IconLoading from '@/components/icons/IconLoading.vue';
import { ref, defineEmits } from 'vue';
import { useAuthStore } from '@/store/auth.js';

const authStore = useAuthStore()
const postContent = ref('')
const error = ref(null)
const isPosting = ref(false)

defineEmits(['close']);

async function createPost() {
  isPosting.value = true
  authStore.setCsrfToken()
  console.log(`csrf from before post ${authStore.csrfToken}`)
  const response = await fetch('https://itter.pythonanywhere.com/api/create/post', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.csrfToken
    },
    body: JSON.stringify({
      content: postContent.value
    }),

  })

  const data = await response.json()

  if (data.error) {
    console.log(data.error)
    error.value = data.error
  } else {
    console.log('success')
    error.value = null
    postContent.value = ''

  }
  isPosting.value = false
}

</script>

<style lang="css" scoped>
.create-post-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.create-post{
  background-color: #2e3440;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
</style>