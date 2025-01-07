<script setup>
import SidebarButton from '@/components/SidebarButton.vue'
import IconSearch from './icons/IconSearch.vue'
import IconProfile from './icons/IconProfile.vue'
import IconHome from './icons/IconHome.vue'
import IconCheck from './icons/IconCheck.vue'
import IconBell from './icons/IconBell.vue'
import { useAuthStore } from "@/store/auth.js"

const authStore = useAuthStore()
</script>

<template>
  <aside class="sidebar">
    <div class="items">
      <div class="icon-panel">
        <ul class="ico">
          <li>
            <SidebarButton :link="{ name: 'home' }">
              Home
              <template #icon>
                <IconHome />
              </template>
            </SidebarButton>
          </li>
          <li>
            <SidebarButton :link="{ name: 'explore' }">
              Explore
              <template #icon>
                <IconSearch />
              </template>
            </SidebarButton>
          </li>
          <li>
            <SidebarButton :link="{ name: 'notifications' }">
              Notifications
              <template #icon>
                <IconBell />
              </template>
            </SidebarButton>
          </li>
          <li>
            <SidebarButton :link="{ name: 'profile' }">
              Profile
              <template #icon>
                <IconProfile />
              </template>
            </SidebarButton>
          </li>
          <li>
            <SidebarButton :link="{ name: 'pricing' }">
              Pro
              <template #icon>
                <IconCheck />
              </template>
            </SidebarButton>
            <SidebarButton @click="authStore.logout">
              Logout
              <template #icon>
                <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m15 9-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
</svg>

              </template>
            </SidebarButton>
          </li>
        </ul>
      </div>
    </div>
    <div class="flex-spacer"></div>
  </aside>
  
</template>

<style lang="css">
.sidebar {
  display: flex;
  gap: 20px;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  position: fixed;
  width: inherit;
}

.flex-spacer{
  flex: 1 1 auto;
}

@media screen and (max-width: 768px) {
  span .btn-text {
    visibility: hidden;
  }
}

.sidebar li {
  font-weight: bold;
}

.sidebar ul {
  list-style-type: none;
}
</style>