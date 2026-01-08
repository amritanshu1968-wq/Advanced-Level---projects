Performance optimization scaffold

Quick start

1. Install dependencies:

```powershell
npm install
```

2. Add your images to `src/assets` (e.g. `sample.jpg`).

3. Prepare (optimize images + build):

```powershell
npm run prepare
```

4. Serve the built `dist` folder and open `http://localhost:8080`:

```powershell
npm run serve
```

5. Optionally run Lighthouse (will launch headless Chrome):

```powershell
npm run lighthouse
```

What this scaffold provides
- Lazy-loading images with `<img loading="lazy">` and `<picture>` using WebP when available.
- Image conversion script (`scripts/convert-images.js`) using `sharp`.
- Bundling & minification via `esbuild`.
- Simple `sw.js` service worker caching core assets.
- Async CSS loading pattern (media=print technique) to reduce render-blocking.
- Lighthouse runner script to generate a `lighthouse-report.html`.

Next steps I can perform for you:
- Run the `prepare` script and `serve` then execute Lighthouse and return the report.
- Tweak service worker caching strategies and add cache-first strategies for images.
- Add critical CSS extraction automation and font-loading optimizations.
