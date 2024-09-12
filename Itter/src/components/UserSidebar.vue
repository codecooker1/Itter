<template>
  <aside class="userbar">
    <form class="max-w-sm mx-auto">
      <label for="message" class="block mb-2 text-sm font-medium text-white">Your message</label>
      <textarea
        id="message"
        rows="4"
        class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
        placeholder="What's on your mind..."
      >
      </textarea>
    </form>
  </aside>
</template>

<script setup></script>

<style>
aside.userbar {
  position: fixed;
}

.userbar {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
  overflow: hidden;
  height: 90vh;
  min-width: 200px;
}

@media screen and (max-width: 1100px) {
  .userbar {
    visibility: collapse;
  }
}
</style>
