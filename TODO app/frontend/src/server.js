const express = require('express');
const path = require('path');
const downloadNewImage = require('./utils/download-new-image')
const fs = require('fs');


const PORT = process.env.PORT || 8000;

const IMAGE_REFRESH_INTERVAL_MIN = parseInt(process.env.IMAGE_REFRESH_INTERVAL_MIN) || 1;
const IMAGE_DOWNLOAD_URL = process.env.IMAGE_DOWNLOAD_URL || 'https://picsum.photos/1200';
const IMAGE_DOWNLOAD_PATH = process.env.IMAGE_DOWNLOAD_PATH || './public/image.jpeg';

if (!fs.existsSync(IMAGE_DOWNLOAD_PATH)) {
    downloadNewImage(IMAGE_DOWNLOAD_URL, IMAGE_DOWNLOAD_PATH)
        .catch(err => console.error(err));
}
setInterval(() => downloadNewImage(IMAGE_DOWNLOAD_URL, IMAGE_DOWNLOAD_PATH), IMAGE_REFRESH_INTERVAL_MIN * 60 * 1000)


const app = express();

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (_, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/image.jpeg', (_, res) => {
    res.sendFile(path.resolve(IMAGE_DOWNLOAD_PATH));
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

