app.get("/create-session", (req, res) => {
    res.cookie(
        "sessionId",
        "user-session-123456"
    );

    res.send("Session created");
});