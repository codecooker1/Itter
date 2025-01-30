<template>
  <div class="profile">
    <div class="profile-header">
      <img :src="profileImage" alt="Profile Image" class="profile-image" />
      <h1 class="profile-name">{{ firstName }} {{ lastName }}</h1>
      <p class="profile-handle">@{{ username }}</p>
    </div>
    <div class="profile-bio">
      <p>{{ bio }}</p>
    </div>
    <div class="profile-stats">
      <div class="stat">
        <span class="stat-number">{{ posts.length }}</span>
        <span class="stat-label">Posts</span>
      </div>
      <div class="stat">
        <span class="stat-number">{{ followers }}</span>
        <span class="stat-label">Followers</span>
      </div>
      <div class="stat">
        <span class="stat-number">{{ following }}</span>
        <span class="stat-label">Following</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import { useAuthStore } from '@/store/auth'

const authStore = useAuthStore()
const profileImage = ref('')
const firstName = ref('')
const lastName = ref('')
const username = ref('')
const bio = ref('')
const posts = ref([])
const followers = ref(0)
const following = ref(0)
const hostname = inject('hostname')

onMounted(async () => {
  profileImage.value = authStore.user.profile_image
  firstName.value = authStore.user.first_name
  lastName.value = authStore.user.last_name
  username.value = authStore.user.username
  bio.value = authStore.user.bio

  const response = await fetch(`${hostname}/api/user/`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  const data = await response.json()
  followers.value = data.followers
  following.value = data.following
  posts.value = data.posts
})
</script>

<style scoped>
.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--bg-nord);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.profile-header {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 10px;
}

.profile-name {
  font-size: 1.8rem;
  font-weight: bold;
  color: var(--text-nord);
}

.profile-handle {
  font-size: 1rem;
  color: var(--text-nord-dark);
}

.profile-bio {
  margin-top: 10px;
  font-size: 1rem;
  color: var(--text-nord-dark);
  text-align: center;
}

.profile-stats {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 20px;
}

.stat {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-number {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--text-nord);
}

.stat-label {
  font-size: 0.9rem;
  color: var(--text-nord-dark);
}
</style>