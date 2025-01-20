<template>
  <div id="create-post-modal">
    <div class="create-post-background" @click="$emit('close')">
      <div class="create-post" @click.stop>
        <h2 class="title">Create a Post</h2>
        <form @submit.prevent="createPost">
          <label for="message" class="block mb-2 text-sm font-medium text-white"></label>
          <textarea v-model="postContent" placeholder="What's on your mind?"
            class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
            rows="5" required></textarea>
          <label for="pi"><i class="fa fa-cloud-upload"></i> Upload Image</label>
          <input style="padding: 0px" @change="handleFileUpload($event)" placeholder="profile_image" id="pi" type="file"
            name="profile_image" accept="image/*" class="textInput" capture>

          <button class="sbutton" type="submit" name="submit">
            <IconLoading v-if="isPosting" /> Post
          </button>
        </form>
        <p v-if="error" class="text-red-500">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import IconLoading from '@/components/icons/IconLoading.vue';
import { ref, defineEmits, onMounted } from 'vue';
import { useAuthStore } from '@/store/auth.js';
import { createClient } from '@supabase/supabase-js';
import { convertImage } from '@/store/helper';
import { nanoid } from 'nanoid';


const authStore = useAuthStore()
const postContent = ref('')
const error = ref(null)
const isPosting = ref(false)
const supabase = ref(null)
const media = ref(null)
const media_url = ref('')

defineEmits(['close']);

onMounted(() => {
  supabase.value = createClient(
    import.meta.env.VITE_SUPABASE_URL,
    import.meta.env.VITE_SUPABASE_KEY
  )
})

async function uploadFile(file) {
  const processedFile = await convertImage(file)

  const { data, error } = await supabase.value.storage
    .from('ItterMedia')
    .upload(`/${authStore.user.username}/`, '' + nanoid(), processedFile)

    if (error) {
        console.error('Error uploading file:', error)
        error.value = error
    } else {
      console.log('File uploaded successfully:', data)
      media_url.value = await this.supabase.storage.from('profilepics').getPublicUrl(data.path).data.publicUrl
      console.log('Public URL:', media_url.value)
    }
}

async function createPost() {
  isPosting.value = true
  authStore.setCsrfToken()
  if(media.value)
    await uploadFile(media.value)
  const response = await fetch('https://itter.pythonanywhere.com/api/create/post', {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.csrfToken,
    },
    body: JSON.stringify({
      content: postContent.value,
      media_url: media_url.value,
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

async function handleFileUpload(event) {
  media.value = event.target.files[0]
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

.create-post {
  background-color: #2e3440;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  width: 600px;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 1.6rem;
}

.create-post > form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  width: 100%;
  font-size: 1rem;
}

.title {
  font-weight: bold;
}

textarea {
  height: auto;
  border-top: 0;
  border-left: 0;
  border-right: 0;
  resize: none;
}

@media screen and (max-width: 768px) {
  .create-post {
    width: calc(100% - 40px);
  }
}

input[type="file"] {
  display: none;
}

#pi {
  border: 1px solid #2e3440;
  /* display: inline-block; */
  padding: 6px 12px;
  cursor: pointer;
  background-color: #232831;
  color: white;
}
</style>