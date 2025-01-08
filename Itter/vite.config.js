import { fileURLToPath, URL } from 'node:url'
import viteCompression from 'vite-plugin-compression';
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    viteCompression({algorithm: 'gzip', verbose: true, threshold: 1501, ext: '.gz'}),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 9000,
    host: true
  }
})
