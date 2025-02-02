<script setup>
import SidebarButton from '@/components/SidebarButton.vue'
import IconSearch from './icons/IconSearch.vue'
import IconProfile from './icons/IconProfile.vue'
import IconHome from './icons/IconHome.vue'
import IconCheck from './icons/IconCheck.vue'
import IconBell from './icons/IconBell.vue'
import IconLogout from './icons/LogoutIcon.vue'
import { useAuthStore } from '@/store/auth.js'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const logout = async () => {
  try {
    await authStore.logout(router)
  } catch (error) {
    console.error(error)
  }
}

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
            <SidebarButton :link="{ name: 'user', params:{username: authStore.user.username }}">
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
            </li>
          <li>
            <SidebarButton link="" @click="logout">
              Logout/Login
              <template #icon>
                <IconLogout />
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

.flex-spacer {
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
