from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

aux = "mongodb+srv://fiuber_admin:gpsvj06RJ1QZVV4t@fiuber."
aux += "qn2hoxw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(aux, 8000)
db = client["clients"]
