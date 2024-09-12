import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NotFound from '@/views/NotFound.vue'
import RtView from '@/components/rtView.vue'
import AboutView from '@/views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/Home',
      name: 'home',
      component: HomeView
    },
    { path: '/gg', component: RtView },
    {
      path: '/Explore',
      name: 'explore',
      component: HomeView
    },
    {
      path: '/Notifications',
      name: 'notifications',
      component: HomeView
    },
    {
      path: '/Profile',
      name: 'profile',
      component: HomeView
    },
    {
      path: '/Pricing',
      name: 'pricing',
      component: HomeView
    },
    {
      path: '/About',
      name: 'about',
      component: AboutView
    },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }
  ]
})

export default router
