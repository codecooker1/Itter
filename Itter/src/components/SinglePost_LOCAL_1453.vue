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
import { ref, onMounted } from 'vue'

//const props = defineProps(["postUrl"]);

const profile_name = ref('default_name')
const profile_handle = ref('default_handle')

async function getPostContent() {
  let url = null
  fetch('http://localhost:8000/api/gettestname/2')
    .then((res) => res.json())
    .then((data) => {
      profile_name.value = data.first_name + ' ' + data.last_name
      profile_handle.value = data.username
    })
  return url
}

const profilePictureUrl = ref(null)

async function getProfilePicture() {
  try {
    const response = await fetch('http://localhost:8000/api/gettestimg')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    const data = await response.json()
    profilePictureUrl.value = data.image_url
  } catch (error) {
    console.error('Error fetching profile picture:', error)
    // Handle error appropriately, e.g., display a default image
    profilePictureUrl.value = '/path/to/default/profile.jpg' // Replace with your default image path
  }
}

onMounted(() => {
  getProfilePicture()
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
