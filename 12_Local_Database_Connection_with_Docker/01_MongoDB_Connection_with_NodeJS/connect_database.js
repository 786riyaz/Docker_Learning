const mongoose = require("mongoose");

// 👉 Replace this with your MongoDB connection string
// const MONGO_URI = "mongodb://localhost:27017/RAFC";
// const MONGO_URI = "mongodb://localhost:27017/RAFC" || "mongodb://host.docker.internal:27017/RAFC";
const MONGO_URI = process.env.MONGO_URI || "mongodb://host.docker.internal:27017/RAFC";

// 1️⃣ Connect to MongoDB
mongoose.connect(MONGO_URI)
.then(() => console.log("✅ Connected to RAFC database"))
.catch((err) => console.error("❌ DB connection error:", err));


// 2️⃣ Define schema for chats collection
const chatSchema = new mongoose.Schema({
    sender: String,
    message: String,
    timestamp: Date
}, { collection: "chats" });  
// 👆 very important: specify { collection: "chats" } to match existing collection


// 3️⃣ Create model
const Chat = mongoose.model("Chat", chatSchema);


// 4️⃣ Fetch all chat documents
async function fetchChats() {
    try {
        const chats = await Chat.find({});
        console.log("📄 Chats from RAFC DB:");
        console.log(chats);
    } catch (error) {
        console.error("❌ Error fetching chats:", error);
    } finally {
        mongoose.connection.close();  // close DB connection
    }
}

fetchChats();
