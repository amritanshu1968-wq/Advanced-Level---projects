const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const srcDir = path.join(__dirname, '..', 'src', 'assets');
const outDir = path.join(__dirname, '..', 'dist', 'assets');
const devDir = srcDir; // Also copy to src/assets for dev server

if (!fs.existsSync(srcDir)) {
  console.error('No src/assets folder found — place images in src/assets and re-run.');
  process.exit(1);
}

fs.mkdirSync(outDir, { recursive: true });

const files = fs.readdirSync(srcDir).filter(f => /\.(jpe?g|png)$/i.test(f));
Promise.all(files.map(f => {
  const srcPath = path.join(srcDir, f);
  const base = path.parse(f).name;
  const outWebp = path.join(outDir, base + '.webp');
  const outCopy = path.join(outDir, f);
  const devWebp = path.join(devDir, base + '.webp');
  return sharp(srcPath)
    .resize({ width: 1200 })
    .toFile(outWebp)
    .then(()=> sharp(srcPath).toFile(outCopy))
    .then(()=> fs.promises.copyFile(outWebp, devWebp)) // Copy webp to src/assets for dev
    .then(()=> console.log('Converted', f))
    .catch(err => console.error('Error', f, err));
})).then(()=> console.log('Image optimization complete'));
