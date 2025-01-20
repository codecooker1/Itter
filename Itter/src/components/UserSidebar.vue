<template>
  <aside class="userbar">
    <form class="max-w-sm mx-auto" @submit.prevent="createPost" method="post">
      <label for="message" class="block mb-2 text-sm font-medium text-white">What's on your mind?</label>
      <textarea id="message " rows="4" v-model="content"
        class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
        placeholder="What's on your mind..." name="message" required></textarea>
        <label for="pi"><i class="fa fa-cloud-upload"></i> Upload Image</label>
          <input style="padding: 0px" @change="handleFileUpload($event)" placeholder="profile_image" id="pi" type="file"
            name="profile_image" accept="image/*" class="textInput" capture>
      <button type="submit" name="submit"> Create Post </button>
    </form>
    <p v-if="error" class="text-red-500">{{ error }}</p>
    <div class="flex-spacer"></div>
  </aside>
</template> 

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/store/auth.js'
import { convertImage } from '@/store/helper.js'
import { nanoid } from 'nanoid'

const error = ref(null)
const authStore = useAuthStore()
const postContent = ref('')
const isPosting = ref(false)
const supabase = ref(null)
const media = ref(null)
const media_url = ref('')

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
  if(media.value){
    await uploadFile(media.value)
  }
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
  }else {
    console.log('success')
    error.value = null
    postContent.value = ''
    
  }
}

async function handleFileUpload(event){
  media.value = event.target.files[0]
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
