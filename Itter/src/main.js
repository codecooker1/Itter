import './assets/index.css'
import './assets/base.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { useHostname } from './composables/useHostname'

const pinia = createPinia()

const app = createApp(App)

const { hostname } = useHostname()

app.provide('hostname', hostname)

app.use(pinia, { hostname })
app.use(router)

app.mount('#app')
