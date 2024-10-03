<template>
  <article>
    <div class="poster-info">
      <IconIncognito size="40px" />
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
import IconIncognito from './icons/IconIncognito.vue'
import LikeButton from './LikeButton.vue';

//const props = defineProps(["likeCount"]);

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
  justify-content: space-between;
  gap: 10px;
  flex-wrap: nowrap;
  height: 42px;
}

.action-bar {
  display: flex;
  flex-direction: row;
  color: red;
  justify-content: space-around;
}
</style>
