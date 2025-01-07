import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {

/**
 * Returns the initial state of the authentication store.
 *
 * The state is loaded from local storage if available; otherwise, it defaults to
 * an unauthenticated state with a null user.
 *
 * @returns {Object} The initial state, with `user` set to null and `isAuthenticated` set to false if not found in local storage.
 */

  state: () => {
    const storedState = localStorage.getItem('authState')
    return storedState
      ? JSON.parse(storedState)
      : {
          user: null,
          isAuthenticated: false
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
      await fetch('http://localhost:8000/api/set-csrf-token', {
        method: 'GET',
        credentials: 'include'
      })
    },

    async login(email, password, router = null) {
      const response = await fetch('http://localhost:8000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCSRFToken()
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
      try {
        const response = await fetch('http://localhost:8000/api/logout', {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCSRFToken()
          },
          credentials: 'include'
        })
        if (response.ok) {
          this.user = null
          this.isAuthenticated = false
          this.saveState()
          if (router) {
            await router.push({ name: 'login' })
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
        const response = await fetch('http://localhost:8000/api/user', {
          credentials: 'include',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
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
          isAuthenticated: this.isAuthenticated
        })
      )
    }
  }
})

/**
 * Gets the CSRF token from the cookie.
 *
 * This is necessary for CSRF protection in Django.
 * @returns {string} The CSRF token.
 * @throws {Error} If the CSRF cookie is missing.
 */
export function getCSRFToken() {
  const name = 'csrftoken'
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  if (cookieValue === null) {
    throw 'Missing CSRF cookie.'
  }
  return cookieValue
}