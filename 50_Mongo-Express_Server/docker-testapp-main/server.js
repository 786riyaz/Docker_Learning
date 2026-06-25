const express = require("express");
const app = express();
const path = require("path");
const MongoClient = require("mongodb").MongoClient;

const PORT = 5050;
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static("public"));

// const MONGO_URL = "mongodb://admin:pass@mongo:27017";
const MONGO_URL = process.env.MONGO_URL;
// const MONGO_URL = "mongodb://localhost:27017";
const client = new MongoClient(MONGO_URL);

//GET all users
app.get("/getUsers", async (req, res) => {
    try {
        const db = client.db("customer-db");
        const data = await db.collection('users').find({}).toArray();
        res.json(data);
    } catch (err) {
        console.error(err);
        res.status(500).send("Server error");
    }
});

//POST new user
app.post("/addUser", async (req, res) => {
    try {
        const userObj = req.body;
        console.log(userObj);
        const db = client.db("customer-db");
        const result = await db.collection('users').insertOne(userObj);
        res.status(201).json({ insertedId: result.insertedId });
    } catch (err) {
        console.error(err);
        res.status(500).send("Insert failed");
    }
});

(async () => {
    try {
        await client.connect();
        console.log('Connected successfully to MongoDB');
        app.listen(PORT, () => {
            console.log(`server running on port ${PORT}`);
        });
    } catch (err) {
        console.error("Failed to start server:", err);
        process.exit(1);
    }
})();

process.on('SIGINT', async () => {
    await client.close();
    process.exit(0);
});