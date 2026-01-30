import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";

export default defineConfig({
  plugins: [react(),  VitePWA({
      registerType: "autoUpdate",
      includeAssets: ["favicon.svg", "robots.txt"],
      manifest: {
        name: "Home Dashboard",
        short_name: "Dashboard",
        description: "Home Assistant Dashboard",
        theme_color: "#121212",
        background_color: "#121212",
        display: "standalone",
        start_url: "/",
        icons: [
          {
            src: "/icons/icon-192.png",
            sizes: "192x192",
            type: "image/png",
          },
          {
            src: "/icons/icon-512.png",
            sizes: "512x512",
            type: "image/png",
          },
        ],
      },
    }),],
  server: {
    host: true,    
    port: 5173,
    watch: {
      ignored: ["**/.env"],
    }
  }
});
