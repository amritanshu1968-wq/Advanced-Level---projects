const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

(async function(){
  try {
    // Build the project first
    console.log('Building the project...');
    await execPromise('npm run build');
    console.log('Build completed.');

    // Start the server
    console.log('Starting server...');
    const serverProcess = exec('npx http-server dist -p 8080 --gzip', { stdio: 'inherit' });

    // Wait for server to start
    await new Promise(resolve => setTimeout(resolve, 3000));

    const url = 'http://localhost:8080';
    console.log('Running Lighthouse on', url);
    // Use Lighthouse CLI
    await execPromise(`npx lighthouse ${url} --output html --output-path lighthouse-report.html --quiet --chrome-flags="--headless"`);
    console.log('Lighthouse audit completed. Report saved to lighthouse-report.html');

    // Kill the server
    serverProcess.kill();
  } catch (error) {
    console.error('Error:', error);
  }
})();
