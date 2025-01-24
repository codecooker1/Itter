<template>
  <aside class="userbar">
    <form class="mx-auto" @submit.prevent="createPost" method="post">
      <label for="message" class="block mb-2 text-sm font-medium text-white">What's on your mind?</label>
      <textarea id="message " rows="4" v-model="postContent"
        class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
        placeholder="What's on your mind..." name="message" required></textarea>
        <label for="pi" @click="triggerFileInput"><i class="fa fa-cloud-upload"></i> Upload Image
          <input style="padding: 0px" @change="handleFileUpload($event)" placeholder="profile_image" id="pi" type="file"
            name="profile_image" accept="image/*" class="textInput" capture></label>
<br><br>
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
import { onMounted, ref, inject } from 'vue'
import { useAuthStore } from '@/store/auth.js'
import { convertImage } from '@/store/helper.js'
import { nanoid } from 'nanoid'
import IconLoading from '@/components/icons/IconLoading.vue'
import { createClient } from '@supabase/supabase-js'

const error = ref(null)
const authStore = ref(useAuthStore())
const postContent = ref('')
const isPosting = ref(false)
const supabase = ref(null)
const media = ref(null)
const media_url = ref('')
const hostname = inject('hostname')

async function uploadFile(file) {
  console.log(`uploading file`)
  const processedFile = await convertImage(file)
  console.log(`file: ${processedFile}`)
  console.log(`usernamr: ${authStore.value.user.username}`)
  const { data, error } = await supabase.value.storage
    .from('ItterMedia')
    .upload(`/${authStore.value.user.username}/${nanoid()}.webp`, processedFile, {contentType: "image/webp"})

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
  authStore.value.setCsrfToken()
  if(media.value){
    await uploadFile(media.value)
  }
  console.log(`csrf from before post ${authStore.value.csrfToken}`)
  const response = await fetch(`${hostname}/api/create/post`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.value.csrfToken
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
  isPosting.value = false
}

async function handleFileUpload(event){
  media.value = event.target.files[0]
}

function triggerFileInput(){
  document.getElementById('pi').click()
}

onMounted(async () => {
  authStore.value = useAuthStore()
  authStore.value.fetchUser()
  supabase.value = createClient(
    import.meta.env.VITE_SUPABASE_URL,
    import.meta.env.VITE_SUPABASE_KEY
  )
})
</script>

<style scoped>
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

.sbutton {
  display: inline-flex;
  gap: 10px;
  align-items: center;
  justify-content: center;
  border: none;
  background-color: #4c566a;
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  font-size: 1rem;
}

</style>
