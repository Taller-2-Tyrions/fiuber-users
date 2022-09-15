from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient("mongodb+srv://fiuber_admin:gpsvj06RJ1QZVV4t@fiuber.qn2hoxw.mongodb.net/?retryWrites=true&w=majority", 8000)
db = client[clients]
