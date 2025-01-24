import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {

  state: () => {
    const storedState = localStorage.getItem('authState')
    return storedState
      ? JSON.parse(storedState)
      : {
          user: null,
          isAuthenticated: false,
          csrfToken: null,
          Host: null,
        }
  },
  actions: {

    async setCsrfToken() {
      this.Host = import.meta.env.VITE_HOSTNAME
      const response = await fetch(`${this.Host}/api/set-csrf-token`, {
        method: 'GET',
        credentials: 'include'
      })
      const data = await response.json()
      this.csrfToken = data.csrfToken
      
    },
    async login(email, password, router = null) {
      this.setCsrfToken()
      const response = await fetch(`${this.Host}/api/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.csrfToken
        },
        body: JSON.stringify({ email, password }),
        credentials: 'include'
      })
      const data = await response.json()
      if (data.success) {
        this.isAuthenticated = true
        this.saveState()
        if (router) {
          await router.push({ name: 'home' })
        }
      } else {
        this.user = null
        this.isAuthenticated = false
        this.saveState()
      }
    },

    /**
     * Logs out the user.
     * This will make a POST request to /api/logout, which will delete the session
     * cookie and log the user out on the backend.
     * If the request fails, it will throw an Error.
     * @param {import('vue-router').Router} [router] - The router to use for
     * redirecting the user after a successful logout.
     * @throws {Error} If the request fails.
     */
    async logout(router = null) {
      this.setCsrfToken()
      try {
        const response = await fetch(`${this.Host}/api/logout`, {
          method: 'POST',
          headers: {
            'X-CSRFToken': this.csrfToken
          },
          credentials: 'include'
        })
        if (response.ok) {
          this.user = null
          this.isAuthenticated = false
          this.saveState()
          if (router) {
            await router.push({ name: 'signin' })
          }
        }
      } catch (error) {
        console.error('Logout failed', error)
        throw error
      }
    },
    

    /**
     * Fetches the user data from the server and updates the state.
     * If the request fails, it sets the state to unauthenticated.
     * @throws {Error} If the request fails.
     */
    async fetchUser() {
      this.setCsrfToken()
      try {
        const response = await fetch(`${this.Host}/api/user`, {
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.csrfToken
          }
        })
        if (response.ok) {
          const data = await response.json()
          this.user = data
          this.isAuthenticated = true
        } else {
          this.user = null
          this.isAuthenticated = false
        }
      } catch (error) {
        console.error('Failed to fetch user\n', error)
        this.user = null
        this.isAuthenticated = false
      }
      this.saveState()
    },

    /**
     * Save the state to local storage.
     *
     * This is a simple way to persist the state when the user reloads the page.
     * For a more robust solution, use pinia-persistent-state.
     */
    saveState() {
      localStorage.setItem(
        'authState',
        JSON.stringify({
          user: this.user,
          isAuthenticated: this.isAuthenticated,
          csrfToken: this.csrfToken,
          Host: this.Host,
        })
      )
    }
  }
})