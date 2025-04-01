import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  build: {
    outDir: '../../../python/minitodo/data/static/',
    emptyOutDir: true,
  },
  server: {
    proxy: {
      // Proxy all /api requests to FastAPI backend
      '/api': {
        target: 'http://localhost:5003',  
        changeOrigin: true,
        secure: false,
      }
    },
    // Handle client-side routing
    historyApiFallback: true
  },
  plugins: [react()],
})
