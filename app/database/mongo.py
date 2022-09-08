from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'), int(os.getenv('MONGO_PORT')))
db = client[os.getenv('MONGO_DB')]