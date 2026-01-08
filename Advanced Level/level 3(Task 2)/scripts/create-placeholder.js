const fs = require('fs');
const path = require('path');

const outDir = path.join(__dirname, '..', 'src', 'assets');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

// 1x1 transparent PNG
const base64 = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=';
const buf = Buffer.from(base64, 'base64');
fs.writeFileSync(path.join(outDir, 'sample.png'), buf);
console.log('Wrote placeholder image to src/assets/sample.png');
