import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {

  /**
   * The state of the authentication store.
   *
   * The state is saved in `localStorage` under the key `authState`.
   *
   * @type {{
   *   user: null | import('~/types').User,
   *   isAuthenticated: boolean,
   *   csrfToken: null | string
   * }}
   */
  state: () => {
    const storedState = localStorage.getItem('authState')
    return storedState
      ? JSON.parse(storedState)
      : {
          user: null,
          isAuthenticated: false,
          csrfToken: null,
        }
  },
  actions: {
    /**
     * Sets the CSRF token for the current session.
     *
     * This is called on every page load to ensure the CSRF token is always
     * up-to-date.
     */
    async setCsrfToken() {
      const response = await fetch('https://itter.pythonanywhere.com/api/set-csrf-token', {
        method: 'GET',
        credentials: 'include'
      })
      const data = await response.json()
      this.csrfToken = data.csrfToken
      document.cookie = `${document.cookie}; csrftoken=${data.csrfToken};`
    },
    async login(email, password, router = null) {
      const response = await fetch('https://itter.pythonanywhere.com/api/login', {
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
        document.cookie = `${document.cookie}; csrftoken=${data.csrfToken}; sessionid=${data.sessionid};`
        console.log(data.csrfToken, data.sessionid)
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
      try {
        const response = await fetch('https://itter.pythonanywhere.com/api/logout', {
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
      try {
        const response = await fetch('https://itter.pythonanywhere.com/api/user', {
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
        console.error('Failed to fetch user', error)
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
        })
      )
    }
  }
})