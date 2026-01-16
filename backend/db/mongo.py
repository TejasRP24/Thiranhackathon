from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["complaint_system"]

complaint_collection = db["complaints"]
task_collection = db["tasks"]
task_history_collection = db["task_status_history"]
sla_breach_collection = db["sla_breaches"]
