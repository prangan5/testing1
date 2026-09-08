// ============================================================
// CI/CD SCANNER TEST 2
// Secure Deserialization
// Fixed Severity: Low
// ============================================================

const express = require('express');
const app = express();

// Middleware to parse JSON bodies safely
app.use(express.json({ limit: '1mb' })); // Adjust limit as needed

app.post('/api/import', (req, res) => {
  const data = req.body.data;

  // Ensure the incoming data is a string that can be safely parsed as JSON
  if (typeof data !== 'string') {
    return res.status(400).json({
      message: 'Invalid input: data must be a JSON string.'
    });
  }

  let userObject;
  try {
    // Use JSON.parse for safe deserialization instead of node-serialize
    userObject = JSON.parse(data);
  } catch (err) {
    // If parsing fails, respond with an error
    return res.status(400).json({
      message: 'Invalid JSON format.',
      error: err.message
    });
  }

  // Optional: Perform additional validation on the parsed object here
  // e.g., ensure required properties exist, types are correct, etc.

  res.json({
    message: 'Data imported successfully',
    data: userObject
  });
});

// Export the app for testing or further integration
module.exports = app;