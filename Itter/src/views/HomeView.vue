<template>
  <div class="structure">
    <div class="usersidebar-wrapper">
      <UserSidebar />
    </div>
    <main class="feedarea">
      <RouterView />
      <button class="create-post-button" @click="triggerCreatePost" v-if="authStore.user"><PenIcon /></button>
    </main>
    <div class="sidebar-wrapper">
      <SidebarView />
    </div>
  </div>
  <CreatePost v-if="createPost" @close="createPost = false" />
</template>

<script setup>
// import SinglePost from '@/components/SinglePost.vue'
import SidebarView from '@/components/SidebarView.vue'
import UserSidebar from '@/components/UserSidebar.vue'
import CreatePost from '@/components/CreatePost.vue'
// import IconQuil from '@/components/icons/IconQuil.vue'
import { ref, inject } from 'vue';
import { useAuthStore } from '@/store/auth';
import PenIcon from '@/components/icons/PenIcon.vue'
import { RouterView, useRouter } from 'vue-router';

const router = useRouter()
const authStore = useAuthStore()
const createPost = ref(false)
// eslint-disable-next-line no-unused-vars
const hostname = inject('hostname')

if(!authStore.isAuthenticated) router.push( { name: 'signin' } )

async function triggerCreatePost(){
  createPost.value = !createPost.value
}
</script>

<style>

.create-post-button {
  border-radius: 50%;
  background-color: #386096;
  float: right;
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 100;
  width: 52px;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  /* visibility: hidden; */
}

.sidebar-wrapper {
  min-width: 200px;
  height: fit-content;
  display: flex;
}

.usersidebar-wrapper {
  min-width: 200px;
  display: flex;
  justify-content: flex-end;
}

.structure {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 15px;
}

.feedarea {
  display: flex;
  flex-direction: column;
  flex: 0 0 auto;
  flex-wrap: nowrap;
  justify-content: flex-start;
  align-items: center;
  max-width: 600px;
  background: var(--bg-nord-secondary);
}

@media screen and (max-width: 1174px) {
  .feedarea {
    width: calc(100% - 285px);
  }

  .sidebar-wrapper {
    min-width: 210px;
  }

  .usersidebar-wrapper {
    display: none;
    visibility: hidden;
  }

  .create-post-button {
    visibility: visible;
  }
}

@media screen and (max-width: 768px) {
  .feedarea {
    width: calc(100% - 55px);
  }

  .sidebar-wrapper {
    min-width: 55px;
  }

  .create-post-button {
    visibility: visible;
  }
}

.post {
  width: 100%;
}

/* width */
::-webkit-scrollbar {
  width: 7px;
}

/* Track */
::-webkit-scrollbar-track {
  background: transparent;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #4c505886;
  border-radius: 15rem;
  border: 2px solid transparent;
  background-clip: padding-box;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #4c505886;
  border: 0;
}
</style>
