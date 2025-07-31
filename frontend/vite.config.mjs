import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve('./src'),
      '@components': path.resolve('./src/components'),
    },
  },
  server: {
    port: 3000,
    open: true,
    // Можно добавить прокси, например:
    // proxy: {
    //   '/api': 'http://localhost:5000'
    // }
  },
  build: {
    outDir: 'dist',       // Папка, куда будет складываться собранный проект (по умолчанию 'dist')
    sourcemap: false,      // Генерировать sourcemaps для удобства отладки в браузере
    minify: 'terser',     // Метод минификации итогового кода, 'terser' — более гибкий, но медленнее, чем 'esbuild'
    emptyOutDir: true,    // Очищать папку outDir перед сборкой, чтобы не оставались старые файлы
    assetsDir: 'assets',  // Папка внутри outDir, куда складываются статические ассеты (картинки, CSS, JS)
    assetsInlineLimit: 0, // Максимальный размер (байты) ассетов, которые будут встроены в JS в base64
    cssCodeSplit: false,   // Разделять CSS на отдельные файлы (если false — весь CSS будет в одном файле)
    chunkSizeWarningLimit: 1600, // Лимит размера чанка (в килобайтах) для предупреждений
    rollupOptions: {      // Дополнительные опции для Rollup (бандлера, на котором основан Vite)
      output: {
        manualChunks: {   // Ручное разделение кода на чанки (чтобы избежать больших бандлов и разделить зависимости)
          vendor: ['react', 'react-dom'],      // Все упомянутые библиотеки будут вынесены в отдельный чанк 'vendor'
          utils: ['lodash', 'axios'],          // lodash и axios соберутся в отдельный чанк 'utils'
        },
      },
    },
  },
  plugins: [
    react(),
    tailwindcss()
  ],
})
