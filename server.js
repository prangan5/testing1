// ============================================================
// CI/CD SCANNER TEST 2
// Insecure Deserialization
// Expected Severity: Critical
// ============================================================

const serialize = require('node-serialize');

app.post('/api/import', (req, res) => {
  const data = req.body.data;

  const userObject = serialize.unserialize(data);

  res.json({
    message: 'Data imported successfully',
    data: userObject
  });
});