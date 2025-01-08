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
        <p>
          Praesent ut sodales nisl. Praesent facilisis libero leo. Phasellus sollicitudin ipsum sit
          amet aliquet malesuada. Quisque eget dui commodo, accumsan mauris vitae, tincidunt lectus.
          Praesent elementum mi quis lorem auctor, sit amet feugiat ligula dignissim. Etiam ac
          sapien malesuada, interdum turpis sollicitudin, varius metus. Proin sit amet ultrices
          magna, eu facilisis massa. Nam risus augue, accumsan eget ante sit amet, tempor vestibulum
          neque. Vestibulum tristique facilisis tortor sit amet sodales. Maecenas cursus iaculis
          lorem at rhoncus. Pellentesque et dui dolor. Ut at bibendum arcu.
        </p>
      </slot>
    </div>
    <div class="media-gallery"></div>
    <div class="action-bar">
      <div class="action-btn">
        <LikeButton />
        <p>123</p>
      </div>
      <p>Repost</p>
      <p>Share</p>
      <p>Comment</p>
    </div>
  </article>
</template>

<script setup>
import ProfileIcon from './icons/ProfileIcon.vue'
import LikeButton from './LikeButton.vue'
import { ref, onActivated, onMounted } from 'vue'
import { useAuthStore } from '@/store/auth.js'

const profile_name = ref('default_name')
const profile_handle = ref('default_handle')
const profilePictureUrl = ref('')

const authstore = useAuthStore()

const user = ref(null)

async function getPostContent() {
  user.value = authstore.user

  if (user.value) {
    profile_name.value = user.value.first_name + ' ' + user.value.last_name
    profile_handle.value = user.value.username
    profilePictureUrl.value = user.value.profile_image
  }
}

onMounted(async () => {
  getPostContent()
})

onActivated(() => {
  console.log('activated')
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
  padding: 16px;
  width: 99%;
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
