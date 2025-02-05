// vite.config.js
import { fileURLToPath, URL } from "node:url";
import viteCompression from "file:///I:/DEV/TwitterClone/t/Itter/Itter/node_modules/vite-plugin-compression2/dist/index.mjs";
import { defineConfig } from "file:///I:/DEV/TwitterClone/t/Itter/Itter/node_modules/vite/dist/node/index.js";
import vue from "file:///I:/DEV/TwitterClone/t/Itter/Itter/node_modules/@vitejs/plugin-vue/dist/index.mjs";
var __vite_injected_original_import_meta_url = "file:///I:/DEV/TwitterClone/t/Itter/Itter/vite.config.js";
var vite_config_default = defineConfig({
  plugins: [
    vue(),
    viteCompression({ algorithm: "gzip", verbose: true, threshold: 1501, ext: ".gz", deleteOriginFile: true })
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", __vite_injected_original_import_meta_url))
    }
  },
  server: {
    port: 9e3,
    host: true
  },
  envDir: "./env",
  envPrefix: "VITE_"
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJJOlxcXFxERVZcXFxcVHdpdHRlckNsb25lXFxcXHRcXFxcSXR0ZXJcXFxcSXR0ZXJcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIkk6XFxcXERFVlxcXFxUd2l0dGVyQ2xvbmVcXFxcdFxcXFxJdHRlclxcXFxJdHRlclxcXFx2aXRlLmNvbmZpZy5qc1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vSTovREVWL1R3aXR0ZXJDbG9uZS90L0l0dGVyL0l0dGVyL3ZpdGUuY29uZmlnLmpzXCI7aW1wb3J0IHsgZmlsZVVSTFRvUGF0aCwgVVJMIH0gZnJvbSAnbm9kZTp1cmwnXHJcbmltcG9ydCB2aXRlQ29tcHJlc3Npb24gZnJvbSAndml0ZS1wbHVnaW4tY29tcHJlc3Npb24yJztcclxuaW1wb3J0IHsgZGVmaW5lQ29uZmlnIH0gZnJvbSAndml0ZSdcclxuaW1wb3J0IHZ1ZSBmcm9tICdAdml0ZWpzL3BsdWdpbi12dWUnXHJcblxyXG4vLyBodHRwczovL3ZpdGVqcy5kZXYvY29uZmlnL1xyXG5leHBvcnQgZGVmYXVsdCBkZWZpbmVDb25maWcoe1xyXG4gIHBsdWdpbnM6IFtcclxuICAgIHZ1ZSgpLFxyXG4gICAgdml0ZUNvbXByZXNzaW9uKHthbGdvcml0aG06ICdnemlwJywgdmVyYm9zZTogdHJ1ZSwgdGhyZXNob2xkOiAxNTAxLCBleHQ6ICcuZ3onLCBkZWxldGVPcmlnaW5GaWxlOiB0cnVlfSksXHJcbiAgXSxcclxuICByZXNvbHZlOiB7XHJcbiAgICBhbGlhczoge1xyXG4gICAgICAnQCc6IGZpbGVVUkxUb1BhdGgobmV3IFVSTCgnLi9zcmMnLCBpbXBvcnQubWV0YS51cmwpKVxyXG4gICAgfVxyXG4gIH0sXHJcbiAgc2VydmVyOiB7XHJcbiAgICBwb3J0OiA5MDAwLFxyXG4gICAgaG9zdDogdHJ1ZVxyXG4gIH0sXHJcbiAgZW52RGlyOiAnLi9lbnYnLFxyXG4gIGVudlByZWZpeDogJ1ZJVEVfJyxcclxufSlcclxuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUFpUyxTQUFTLGVBQWUsV0FBVztBQUNwVSxPQUFPLHFCQUFxQjtBQUM1QixTQUFTLG9CQUFvQjtBQUM3QixPQUFPLFNBQVM7QUFIcUssSUFBTSwyQ0FBMkM7QUFNdE8sSUFBTyxzQkFBUSxhQUFhO0FBQUEsRUFDMUIsU0FBUztBQUFBLElBQ1AsSUFBSTtBQUFBLElBQ0osZ0JBQWdCLEVBQUMsV0FBVyxRQUFRLFNBQVMsTUFBTSxXQUFXLE1BQU0sS0FBSyxPQUFPLGtCQUFrQixLQUFJLENBQUM7QUFBQSxFQUN6RztBQUFBLEVBQ0EsU0FBUztBQUFBLElBQ1AsT0FBTztBQUFBLE1BQ0wsS0FBSyxjQUFjLElBQUksSUFBSSxTQUFTLHdDQUFlLENBQUM7QUFBQSxJQUN0RDtBQUFBLEVBQ0Y7QUFBQSxFQUNBLFFBQVE7QUFBQSxJQUNOLE1BQU07QUFBQSxJQUNOLE1BQU07QUFBQSxFQUNSO0FBQUEsRUFDQSxRQUFRO0FBQUEsRUFDUixXQUFXO0FBQ2IsQ0FBQzsiLAogICJuYW1lcyI6IFtdCn0K
