import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router'
import store from './store'
import axios from './api/index.js'

const app = createApp(App)
app.use(ElementPlus).use(router).use(store).mount('#app')

app.config.globalProperties.axios = axios