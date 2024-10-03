<template>
  <aside class="userbar">
    <form class="max-w-sm mx-auto">
      <label for="message" class="block mb-2 text-sm font-medium text-white">Your message</label>
      <textarea id="message" rows="4"
        class="block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500"
        placeholder="What's on your mind...">
      </textarea>
      <input type="submit" />
    </form>
  </aside>
</template>

<script setup></script>

<style>
.userbar {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
  gap: 20px;
  overflow: hidden;
  width: inherit;
  position: fixed;
}
</style>
