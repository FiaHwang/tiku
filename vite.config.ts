import { defineConfig } from 'vite';
import { resolve, extname } from 'path';
import { readdirSync, statSync } from 'fs';
import { fileURLToPath } from 'url';

// Helper to handle ESM path resolution
const __filename = fileURLToPath(import.meta.url);
const __dirname = resolve(__filename, '..');

// Helper function to recursively find all HTML files in the project directories
function getHtmlFiles(dir: string, baseDir: string = dir): Record<string, string> {
  const files: Record<string, string> = {};
  
  function traverse(currentDir: string) {
    const list = readdirSync(currentDir);
    for (const file of list) {
      const filePath = resolve(currentDir, file);
      const stat = statSync(filePath);
      
      if (stat.isDirectory()) {
        // Exclude dependency, build, and hidden directories
        if (file !== 'node_modules' && file !== 'dist' && !file.startsWith('.')) {
          traverse(filePath);
        }
      } else if (stat.isFile() && extname(file) === '.html') {
        const relativePath = filePath.substring(baseDir.length + 1);
        const key = relativePath.replace(/\.html$/, '').replace(/\\/g, '/');
        files[key] = filePath;
      }
    }
  }
  
  traverse(dir);
  return files;
}

export default defineConfig({
  server: {
    port: 3000,
    host: '0.0.0.0',
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: getHtmlFiles(__dirname),
    },
  },
});

