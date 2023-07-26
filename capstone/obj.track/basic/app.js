const express = require('express');
const mjpegProxy = require('mjpeg-proxy');

const app = express();
const port = 3000;

// Serve the HTML page
app.get('/', (req, res) => {
  res.send(`
    <html>
      <body>
        <h1>MJPEG Stream</h1>
        <img src="http://localhost:8000" width="640" height="480" />
      </body>
    </html>
  `);
});

// Proxy the MJPEG stream from localhost:8000 to /mjpeg
app.use('/mjpeg', mjpegProxy('http://localhost:8000'));

// Start the server
app.listen(port, () => {
  console.log(`Server started at http://localhost:${port}`);
});
