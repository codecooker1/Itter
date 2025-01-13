<template>
  <div class="form-holder">
    <div class="form-box">
      <span class="title">Register</span>
      <form @submit.prevent="signin" class="form">
        <div class="textInputWrapper">
          <label for="email">E-mail</label>
          <input
            v-model="email"
            placeholder="E-mail"
            type="email"
            id="email"
            name="email"
            class="textInput"
            required
          />
        </div>
        <div class="textInputWrapper">
          <label for="password">Password</label>
          <input
            v-model="password"
            placeholder="Password"
            id="password"
            type="password"
            name="password"
            class="textInput"
            required
          />
        </div>
        <button class="sbutton" type="submit">Login</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </div>
</template>

<style>
.form-holder {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
  background-color: #00000011;
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
  margin: 12px 5px;
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

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/store/auth'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const error = ref('')

const authStore = useAuthStore()
const router = useRouter()

const signin = async () => {
  try {
    await authStore.login(email.value, password.value, router)
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  await authStore.fetchUser()
})
</script>
