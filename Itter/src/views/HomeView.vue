<template>
  <div class="structure">
    <div class="usersidebar-wrapper">
      <UserSidebar />
    </div>
    <main class="feedarea">
      <div class="h-2"></div>
      <div class="post" v-for="post in posts" :key="post.ipost_id">
        <SinglePost :post="post" />
      </div>
      
    </main>
    <div class="sidebar-wrapper">
      <SidebarView />
      <button class="sbutton" @click="createPost = !createPost">Create Post</button>
    </div>
  </div>
  <CreatePost v-if="createPost" />
</template>

<script setup>
import SinglePost from '@/components/SinglePost.vue'
import SidebarView from '@/components/SidebarView.vue'
import UserSidebar from '@/components/UserSidebar.vue'
import CreatePost from '@/components/CreatePost.vue';
import { onMounted, ref } from 'vue';
import { useAuthStore } from '@/store/auth';

const posts = ref([])
const authStore = useAuthStore()
const createPost = ref(false)

onMounted(async () => {
  const response = await fetch('https://itter.pythonanywhere.com/api/feed/', {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.csrfToken,
      'Accept-Encoding': 'gzip, deflate, br',
    },
    })
  const data = await response.json()
  posts.value = data.posts
  console.log(posts)
})
</script>

<style>
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
  gap: 20px;
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
}

@media screen and (max-width: 768px) {
  .feedarea {
    width: calc(100% - 55px);
  }

  .sidebar-wrapper {
    min-width: 55px;
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
