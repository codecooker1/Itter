<template>
  <div class="feed-structure">
    <main class="feed-area">
      <div class="h-2"></div>
      <div class="post" v-for="post in posts" :key="post.post_id">
        <SinglePost :post_id="post.post_id" />
      </div>
    </main>
  </div>
</template>

<script setup>
import SinglePost from '@/components/SinglePost.vue';
import { onMounted, ref, inject } from 'vue';
import { useAuthStore } from '@/store/auth';

const posts = ref([]);
const authStore = useAuthStore();
const hostname = inject('hostname');

onMounted(async () => {
  const response = await fetch(`${hostname}/api/feed/`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.csrfToken,
      'Accept-Encoding': 'gzip, deflate, br',
    },
  });
  const data = await response.json();
  posts.value = data.posts;
});
</script>

<style>
.feed-structure {
  display: flex;
  justify-content: center;
  gap: 15px;
}

.feed-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 600px;
  background: var(--bg-nord-secondary);
}

.post {
  width: 100%;
}
</style>
