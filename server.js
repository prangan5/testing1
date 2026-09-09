app.get("/process", (req, res) => {
    try {
        const input = JSON.parse(
            req.query.data
        );

        res.json(input);

    } catch (error) {
        res.status(500).json({
            error: error.message,
            stack: error.stack
        });
    }
});