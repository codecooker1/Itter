<script setup>
import SidebarButton from '@/components/SidebarButton.vue'
import IconSearch from './icons/IconSearch.vue'
import IconProfile from './icons/IconProfile.vue'
import IconHome from './icons/IconHome.vue'
import IconCheck from './icons/IconCheck.vue'
import IconBell from './icons/IconBell.vue'
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
          </li>
        </ul>
      </div>
    </div>
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
}
@media screen and (max-width: 768px) {
  span .btn-text {
    visibility: hidden;
  }
  .sidebar {
    width: 55px;
  }
}
.sidebar li {
  font-weight: bold;
}
.sidebar ul {
  list-style-type: none;
}
/*
.items {
  margin: 15px;
  padding: 25px;
}*/
</style>
