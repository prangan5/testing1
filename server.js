app.get("/debug-info", (req, res) => {
    res.json({
        environment: process.env,
        nodeVersion: process.version,
        platform: process.platform,
        workingDirectory: process.cwd()
    });
});