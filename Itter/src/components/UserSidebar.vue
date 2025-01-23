<template>
  <aside class="userbar">
    <form class="mx-auto" @submit.prevent="createPost" method="post">
      <label for="message" class="block mb-2 text-sm font-medium text-white">What's on your mind?</label>
      <textarea id="message " rows="4" v-model="content"
        class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
        placeholder="What's on your mind..." name="message" required></textarea>
        <label for="pi" @click="triggerFileInput"><i class="fa fa-cloud-upload"></i> Upload Image
          <input style="padding: 0px" @change="handleFileUpload($event)" placeholder="profile_image" id="pi" type="file"
            name="profile_image" accept="image/*" class="textInput" capture></label>

            <button class="sbutton" type="submit" name="submit">
            <IconLoading v-if="isPosting" /> Create Post
          </button>
    </form>
    <p v-if="error" class="text-red-500">{{ error }}</p>
    <div class="flex-spacer"></div>

    <div class="user">
      <div class="user-image">
        <img :src="authStore.user.profile_image" alt="User Profile Image" />
      </div>
      <div class="user-info">
        <h2>{{ authStore.user.username }}</h2>
        <p>{{ authStore.user.email }}</p>
      </div>
    </div>
  </aside>
</template> 

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/store/auth.js'
import { convertImage } from '@/store/helper.js'
import { nanoid } from 'nanoid'
import IconLoading from '@/components/icons/IconLoading.vue'

const error = ref(null)
const authStore = useAuthStore()
const postContent = ref('')
const isPosting = ref(false)
const supabase = ref(null)
const media = ref(null)
const media_url = ref('')

async function uploadFile(file) {
  console.log(`uploading file`)
  const processedFile = await convertImage(file)
  console.log(`file: ${processedFile}`)
  console.log(`usernamr: ${authStore.user.username}`)
  const { data, error } = await supabase.value.storage
    .from('ItterMedia')
    .upload(`/${authStore.user.username}/${nanoid()}.webp`, processedFile, {contentType: "image/webp"})

  if (error) {
    console.error('Error uploading file:', error)
    error.value = error
  } else {
    console.log('File uploaded successfully:', data)
    media_url.value = await supabase.value.storage.from('ItterMedia').getPublicUrl(data.path).data.publicUrl
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

function triggerFileInput(){
  document.getElementById('pi').click()
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
  height: 100vh;
  padding: 20px 0 20px 0;
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

.user {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  margin-top: auto;
}

.user-image {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 10px;
}

.user-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info h2 {
  font-size: 18px;
  margin: 0;
}

.user-info p {
  font-size: 14px;
  margin: 0;
}

.user-info {
  text-align: right;
}
</style>
