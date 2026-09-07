const express = require('express');
const app = express();

let token = 'ghp_dummyPlaintextGithubTokenForTesting';

app.get('/', (req, res) => {
  res.send('Hello');
});

app.listen(3000);
