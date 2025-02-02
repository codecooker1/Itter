<template>
  <div class="profile">
    <div class="profile-header">
      <img :src="profileImage" alt="Profile Image" class="profile-image" />
      <h1 class="profile-name">{{ firstName }} {{ lastName }}</h1>
      <p class="profile-handle">@{{ username }}</p>
      <button @click="followUser" class="follow-button">{{ followtext }}</button>
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
  <div class="post" v-for="post in posts" :key="post.post_id">
        <SinglePost :post_id="post.post_id" />
  </div>
</template>

<script setup>
import { ref, onMounted, inject,  } from 'vue'
import { useAuthStore } from '@/store/auth'
import { useRoute } from 'vue-router'
import SinglePost from '@/components/SinglePost.vue'

const profileImage = ref('')
const firstName = ref('')
const lastName = ref('')
const username = ref('')
const bio = ref('')
const posts = ref([])
const followers = ref(0)
const following = ref(0)
const hostname = inject('hostname')
const route = useRoute()
const authStore = useAuthStore()
const followtext = ref('Follow')
const is_following = ref(false)

onMounted(async () => {
  const response = await fetch(`${hostname}/api/user/detail/${route.params.username}`, {
    method: 'GET',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
    },
  })

  const data = await response.json()

  profileImage.value = data.profile_image
  firstName.value = data.first_name
  lastName.value = data.last_name
  username.value = data.username
  bio.value = data.bio
  followers.value = data.followers
  following.value = data.following
  posts.value = data.posts
  is_following.value = data.is_following
  followtext.value = is_following.value ? 'Unfollow' : 'Follow'
})

async function followUser() {
  const response = await fetch(`${hostname}/api/user/follow/${route.params.username}`, {
    method: 'POST',
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authStore.csrfToken,
    },
  })
  const data = await response.json() 
  
  if (data){
    is_following.value = !is_following.value
    followtext.value = is_following.value ? 'Unfollow' : 'Follow'
  }

  console.log(data)
}
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
  min-width: 600px;
  border-radius: 15px;
  height: calc(fit-content + 40px);
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