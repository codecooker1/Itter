<template>
  <div class="form-holder">
    <div class="form-box">
      <span class="title">Register</span>
      <form @submit.prevent="register" class="form">
        <div class="textInputWrapper">
          <label for="firstname">First Name</label>
          <input v-model="firstname" placeholder="First Name" type="text" id="firstname" name="firstname"
            class="textInput" required />
        </div>
        <div class="textInputWrapper">
          <label for="lastname">Last Name</label>
          <input v-model="lastname" placeholder="Last name" type="text" id="lastname" name="lastname" class="textInput"
            required />
        </div>
        <div class="textInputWrapper">
          <label for="username">Username</label>
          <input v-model="username" placeholder="Username" id="username" type="text" name="username" class="textInput"
            required />
        </div>
        <div class="textInputWrapper">
          <label for="email">E-mail</label>
          <input v-model="email" placeholder="E-mail" type="email" id="email" name="email" class="textInput" required />
        </div>
        <div class="textInputWrapper">
          <label for="password">Password</label>
          <input v-model="password" placeholder="Password" id="password" type="password" name="password"
            class="textInput" required />
        </div>
        <div class="textInputWrapper">
          <label for="bio">Tell something about yourself</label>
          <input v-model="bio" placeholder="Tell about yourself" id="bio" type="textbox" name="bio" class="textInput"
            required />
        </div>
        <div class="textInputWrapper">
          <label for="pi">Profile Image</label>
          <input style="padding: 0px" @change="handleFileUpload($event)" placeholder="profile_image" id="pi" type="file"
            name="profile_image" accept="image/*" class="textInput" required capture />
          <!-- <img v-if="this.imageUrl" :src="this.imageUrl" alt="Selected Image" style="max-width: 200px; max-height: 200px; margin-top: 10px;"> -->
          <p>{{ uploadError }}</p>
        </div>
        <button class="sbutton" type="submit" name="submit">
          <IconLoading v-if="isRegistering" /> Register
        </button>
      </form>
      <p v-if="error" class="text-red-500">{{ error }}</p>
      <p v-if="success" class="text-green-300">{{ success }}</p>
    </div>
  </div>
</template>

<style scoped>
.form-holder {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  /* background-color: #00000011; */
}

.form-box {
  height: 100vh;
  max-width: 600px;
}

.form {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 20px;
  background-color: var(--accent-color);
  border-radius: 24px;
}

.title {
  font-weight: bold;
  font-size: 1.6rem;
}

/* From Uiverse.io by Kabak */
.sbutton {
  height: 50px;
  margin: 5px;
  width: 120px;
  background: #333;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  cursor: pointer;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  font-family:
    Consolas,
    Courier New,
    monospace;
  border: solid #404c5d 1px;
  font-size: 16px;
  color: rgb(161, 161, 161);
  -webkit-transition: 500ms;
  transition: 500ms;
  border-radius: 15px;
  background: linear-gradient(145deg, #2e2d2d, #212121);
  -webkit-box-shadow:
    -1px -5px 15px #41465b,
    5px 5px 15px #41465b,
    inset 5px 5px 10px #212121,
    inset -5px -5px 10px #212121;
  box-shadow:
    -1px -5px 15px #41465b,
    5px 5px 15px #41465b,
    inset 5px 5px 10px #212121,
    inset -5px -5px 10px #212121;
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

.sbutton:hover {
  -webkit-box-shadow:
    1px 1px 13px #20232e,
    -1px -1px 13px #545b78;
  box-shadow:
    1px 1px 13px #20232e,
    -1px -1px 13px #545b78;
  color: #d6d6d6;
  -webkit-transition: 500ms;
  transition: 500ms;
}

.sbutton:active {
  -webkit-box-shadow:
    1px 1px 13px #20232e,
    -1px -1px 33px #545b78;
  box-shadow:
    1px 1px 13px #20232e,
    -1px -1px 33px #545b78;
  color: #d6d6d6;
  -webkit-transition: 100ms;
  transition: 100ms;
}

/* From Uiverse.io by WhiteNervosa */
.textInputWrapper {
  position: relative;
  width: 100%;
  /* 180px;*/
  min-width: 180px;
  margin: 6px 5px;
  --accent-color: #a3e583;
}

.textInputWrapper:before {
  transition: border-bottom-color 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border-bottom: 1px solid rgba(0, 0, 0, 0.42);
}

.textInputWrapper:before,
.textInputWrapper:after {
  content: '';
  left: 0;
  right: 0;
  position: absolute;
  pointer-events: none;
  bottom: -1px;
  z-index: 4;
  width: 100%;
}

.textInputWrapper:focus-within:before {
  border-bottom: 1px solid var(--accent-color);
}

.textInputWrapper:before {
  transition: border-bottom-color 200ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  border-bottom: 1px solid rgba(0, 0, 0, 0.42);
}

.textInputWrapper:focus-within:before {
  border-bottom: 1px solid var(--accent-color);
  transform: scaleX(1);
}

.textInputWrapper:focus-within:after {
  border-bottom: 2px solid var(--accent-color);
  transform: scaleX(1);
}

.textInputWrapper:after {
  content: '';
  transform: scaleX(0);
  transition: transform 250ms cubic-bezier(0, 0, 0.2, 1) 0ms;
  will-change: transform;
  border-bottom: 2px solid var(--accent-color);
  border-bottom-color: var(--accent-color);
}

.textInput::placeholder {
  transition: opacity 250ms cubic-bezier(0, 0, 0.2, 1) 0ms;
  opacity: 1;
  user-select: none;
  color: rgba(255, 255, 255, 0.582);
}

.textInputWrapper .textInput {
  border-radius: 5px 5px 0px 0px;
  box-shadow: 0px 2px 5px rgb(35 35 35 / 30%);
  max-height: 36px;
  background-color: #252525;
  transition-timing-function: cubic-bezier(0.25, 0.8, 0.25, 1);
  transition-duration: 200ms;
  transition-property: background-color;
  color: #e8e8e8;
  font-size: 14px;
  font-weight: 500;
  padding: 12px;
  width: 100%;
  border-left: none;
  border-bottom: none;
  border-right: none;
}

.textInputWrapper .textInput:focus,
.textInputWrapper .textInput:active {
  outline: none;
}

.textInputWrapper:focus-within .textInput,
.textInputWrapper .textInput:focus,
.textInputWrapper .textInput:active {
  background-color: #353535;
}

.textInputWrapper:focus-within .textInput::placeholder {
  opacity: 0;
}
</style>

<script>
// eslint-disable-next-line no-unused-vars
import IconLoading from '@/components/icons/IconLoading.vue'
import { useAuthStore } from '@/store/auth'
import { createClient } from '@supabase/supabase-js'
import { nanoid } from 'nanoid'
import { convertImage } from '@/store/helper'
import { inject } from 'vue'


export default {
  data() {
    return {
      firstname: '',
      lastname: '',
      username: '',
      email: '',
      password: '',
      bio: '',
      profile_image: '',
      error: '',
      success: '',
      selectedFile: null,
      supabase: null,
      uploadError: '',
      authStore: '',
      isRegistering: false,
      hostname: inject('hostname')
    }
  },

  mounted() {
    this.supabase = createClient(
      import.meta.env.VITE_SUPABASE_URL,
      import.meta.env.VITE_SUPABASE_KEY
    )
    this.authStore = useAuthStore()
    this.authStore.setCsrfToken()
  },

  methods: {
    /**
     * Uploads a file to the Supabase storage and sets the profile_image
     * to the public URL of the uploaded file.
     * @param {File} file - The file to be uploaded
     * @return {Promise<void>}
     */
    async uploadFile(file) {
      const fileToUpload = await convertImage(file)
      const { data, error } = await this.supabase.storage
        .from('profilepics')
        .upload('/' + nanoid(), fileToUpload, { contentType: fileToUpload.type })
      if (error) {
        console.error('Error uploading file:', error)
      } else {
        console.log('File uploaded successfully:', data)
        this.profile_image = await this.supabase.storage.from('profilepics').getPublicUrl(data.path)
          .data.publicUrl
        console.log('Public URL:', this.profile_image)
      }
    },
    async register() {
      try {
        this.isRegistering = true
        await this.uploadFile(this.selectedFile)
        console.log(this.authStore.csrfToken)

        const response = await fetch(`${this.hostname}/api/create-user/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.authStore.csrfToken
          },
          body: JSON.stringify({
            firstname: this.firstname,
            lastname: this.lastname,
            email: this.email,
            password: this.password,
            bio: this.bio,
            username: this.username,
            profile_image: this.profile_image
          }),
          credentials: 'include'
        })
        const data = await response.json()
        if (response.ok) {
          this.success = 'Registration successful! Please Check your email for verification link to continue.'
        } else {
          this.error = data.error || 'Registration failed'
        }
        this.isRegistering = false
      } catch (err) {
        this.error = 'An error occurred during registration: ' + err
      }
    },
    async handleFileUpload(event) {
      this.selectedFile = event.target.files[0]
      console.log(this.selectedFile)
      this.uploadError = null
      this.uploadSuccess = null

      if (this.selectedFile) {
        if (!this.selectedFile.type.startsWith('image/')) {
          this.uploadError = 'Please select a Proper image.'
          this.selectedFile = null
          this.imageUrl = null
          return
        }
        this.imageUrl = URL.createObjectURL(this.selectedFile)
      } else {
        this.imageUrl = null
      }
    },
  }
}
</script>
