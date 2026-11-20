import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()

uri = os.getenv("MONGO_DB_URL")

client = MongoClient(
    uri,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print("Connection failed:", e)
finally:
    client.close()