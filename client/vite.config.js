import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
    server: {
        host: '0.0.0.0',  // Allows connections from Docker
        port: 5173,
        strictPort: true,
        watch: {
            usePolling: true, // Ensures file changes are detected inside Docker
        },
        hmr: {
            clientPort: 5173, // Ensures WebSocket connection works correctly
            host: 'localhost', // Use 'localhost' or replace with the Nginx proxy hostname
        },
    },
});
