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
    <div v-if="media" class="media-gallery"><image :src="media" /></div>
    <div class="action-bar">
      <div class="action-btn">
        <LikeButton />
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
import { ref, onMounted } from 'vue'
// import { useAuthStore } from '@/store/auth.js'

const profile_name = ref('default_name')
const profile_handle = ref('default_handle')
const profilePictureUrl = ref('')
const content = ref('')
const media = ref('')
const likes = ref(0)

// const authstore = useAuthStore()

// const user = ref(null)

const props = defineProps(['post'])

async function getPostContent() {
  console.log(props.post)
  profile_name.value = props.post.user.first_name + ' ' + props.post.user.last_name
  profile_handle.value = props.post.user.username
  profilePictureUrl.value = props.post.user.profile_image
  content.value = props.post.content
  media.value = props.post.image
  likes.value = props.post.likes
}

onMounted(async () => {
  getPostContent()
})
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
</style>
