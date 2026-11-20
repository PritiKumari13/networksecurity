from pymongo.mongo_client import MongoClient
import certifi

uri = "mongodb+srv://p0311182_db_user:Priti123@cluster0.mihijfs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, tlsCAFile=certifi.where())

try:
    client.admin.command("ping")
    print("Successfully connected to Priti's MongoDB Atlas!")
except Exception as e:
    print("Connection failed:", e)
finally:
    client.close()