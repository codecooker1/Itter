<template>
  <article>
    <div class="poster-info">
      <ProfileIcon :picUrl="profilePictureUrl" />
      <div class="info">
        <p>{{ profile_name }}</p>
        <p class="handle">@{{ profile_handle }}</p>
      </div>
    </div>
    <div class="main-post">
      <slot>
        <br>
        <div>{{ content }}</div>
        <br>
      </slot>
    </div>
    <div v-if="media" class="media-gallery"><img :src="media" alt="Unable to load Image" /></div>
    <div class="h-2"></div>
    <div class="action-bar">
      <div class="action-btn">
        <LikeButton @click="likePost" :isLiked="isLiked" />
        <p>{{ likes }}</p>
      </div>
      <!-- <p>Repost</p>
      <p>Share</p>
      <p>Comment</p> -->
    </div>
  </article>
</template>

<script setup>
import ProfileIcon from './icons/ProfileIcon.vue'
import LikeButton from './LikeButton.vue'
import { ref, inject, onBeforeMount, provide } from 'vue'
import { useAuthStore } from '@/store/auth.js'

const profile_name = ref('default_name')
const profile_handle = ref('default_handle')
const profilePictureUrl = ref('')
const content = ref('')
const media = ref('')
const likes = ref(0)
const isLiked = ref(false)
const hostname = inject('hostname')

const authstore = useAuthStore()

provide('liked', isLiked)

// const user = authstore.user

const props = defineProps(['post_id'])

async function getPostContent() {
  console.log(props.post_id)
  const request = await fetch(`${hostname}/api/post/detail/${props.post_id}`, {
    method: "GET",
    credentials: "include",
  })
  const post = await request.json()
  profile_name.value = post.user.first_name + ' ' + post.user.last_name
  profile_handle.value = post.user.username
  profilePictureUrl.value = post.user.profile_image
  content.value = post.content
  media.value = post.image
  likes.value = post.likes
  isLiked.value = post.is_liked
  console.log(isLiked.value)
}

onBeforeMount(async () => {
  getPostContent()
  setInterval(updateLikeCount, 50000)
})

async function likePost() {
  console.log(props.post_id) 
  const response = await fetch(`${hostname}/api/like/post/`, {
      method: "POST",
      credentials: "include",
      headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': authstore.csrfToken,
      },
      body: JSON.stringify({
        post_id: props.post_id,
      }),
  })

  const data = await response.json()

  console.log(data)
  if(isLiked.value) likes.value -= 1
  else likes.value += 1

  isLiked.value = !isLiked.value
}

async function updateLikeCount(){
  const response = await fetch(`${hostname}/api/post/detail/${props.post_id}`)
  const post = await response.json()
  likes.value = post.likes
}
</script>

<style scoped>
article {
  display: block;
  border-bottom: 1px solid var(--border-nord);
  background-color: #2e3440;
  /*#222222;*/
  min-height: 54px;
  margin: 2px;
  padding: 16px;
  overflow-wrap: break-word;
}

/* @media screen and (max-width: 1174px) {
  article {
    width: calc(100% - 4px);
  }
}

@media screen and (max-width: 768px) {
  article {
    width: calc(100% - 2px);
  }
} */

.main-post {
  width: 100%;
}

.action-btn {
  display: ruby;
  font-size: 12px;
}

.poster-info {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 10px;
  flex-wrap: nowrap;
}

.info {
  display: inline-flex;
  line-height: 1em;
  color: #fff;
  flex-direction: column;
  align-items: space-around;
}

.info .handle {
  color: #b5bbc4;
  font-size: 0.9em;
}

.action-bar {
  display: flex;
  flex-direction: row;
  color: red;
  justify-content: space-around;
}

.media-gallery img {
  border-radius: 11px;
}
</style>
