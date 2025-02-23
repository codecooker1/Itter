import { createRouter, createWebHistory } from 'vue-router'
const HomeView = () => import('@/views/HomeView.vue')
const NotFound = () => import('@/views/NotFound.vue')
const RtView = () => import('@/components/rtView.vue')
const AboutView = () => import('@/views/AboutView.vue')
const SignupView = () => import('@/views/SignupView.vue')
const SigninView = () => import('@/views/SigninView.vue')
const TestComponent = () => import('@/components/CreatePost.vue')
const ProfileView = () => import('@/views/nested/ProfileView.vue')
const FeedView = () => import('@/views/nested/FeedView.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/Signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/Signin',
      name: 'signin',
      component: SigninView
    },
    {
      path: '/',
      component: HomeView,
      children:[
        {
          path: '',
          name: 'home',
          component: FeedView,
        },
        { 
          path: 'u/:username',
          name  : 'user',
          component: ProfileView,
          // meta: { transition: 'slide-left' },
        },
      ]
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
      path: '/Pricing',
      name: 'pricing',
      component: HomeView
    },
    {
      path: '/About',
      name: 'about',
      component: AboutView
    },
    {
      path: '/test',
      name: 'test-components',
      component: TestComponent
    },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }
  ]
})

export default router
