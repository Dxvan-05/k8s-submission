const express = require('express');


const PORT = process.env.PORT || 8000;

const app = express();

app.get('/', (_, res) => {
    res.send(`Server running on port ${PORT}`)
})

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

