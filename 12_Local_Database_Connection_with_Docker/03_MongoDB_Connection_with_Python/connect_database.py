# pip install pymongo

from pymongo import MongoClient
import os
import sys

# 👉 Replace this with your MongoDB connection string or set MONGO_URI env var
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://host.docker.internal:27017/RAFC")
# MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/RAFC")

def connect_db(uri: str):
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        # trigger server selection to validate connection
        client.server_info()
        print("✅ Connected to RAFC database")
        return client
    except Exception as e:
        print("❌ DB connection error:", e, file=sys.stderr)
        raise

def fetch_chats(db):
    try:
        chats = list(db["chats"].find({}))
        print("📄 Chats from RAFC DB:")
        for c in chats:
            print(c)
    except Exception as e:
        print("❌ Error fetching chats:", e, file=sys.stderr)
    finally:
        # close DB connection
        db.client.close()

if __name__ == "__main__":
    client = connect_db(MONGO_URI)
    # if MONGO_URI supplies a DB name (e.g. mongodb://.../RAFC), use get_default_database()
    try:
        db = client.get_default_database() or client["RAFC"]
    except Exception:
        # fallback to explicit database name
        db = client["RAFC"]

    fetch_chats(db)
