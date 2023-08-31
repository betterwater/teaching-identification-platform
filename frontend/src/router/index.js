import { createRouter, createWebHistory } from 'vue-router';
import App from '../App.vue'
import Education from '../Education.vue'

const routes = [
    {
        path: '/',
        redirect: '/App'
    },
    {
        name: 'App',
        path: '/app',
        component: App,
    },
    {
        name: 'Education',
        path: '/education',
        component: Education
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router;
