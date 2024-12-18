import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from 'path';

export default defineConfig({
  base: process.env.NODE_ENV == "production" ? "/static/" : "/",
  plugins: [vue()],
  server: {
    host: 'frontend',
    port: 5173
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
});
