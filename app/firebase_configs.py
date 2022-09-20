import pyrebase
import firebase_admin
from firebase_admin import credentials
import json
import os

if (os.getenv("FIREBASE_KEY")):
    cred = credentials.Certificate(json.loads(os.getenv("FIREBASE_KEY")))
else:
    cred = credentials.Certificate("firebasekey.json")

firebase = firebase_admin.initialize_app(cred)

firebaseConfig = {
    "apiKey": "AIzaSyDQggb3aFCUpnBb8Dm2bRNoh49G5Pn1pIM",
    "authDomain": "fiuber-develop.firebaseapp.com",
    "projectId": "fiuber-develop",
    "storageBucket": "fiuber-develop.appspot.com",
    "messagingSenderId": "413252036613",
    "appId": "1:413252036613:web:c3bbbe1caae2b9078b546c",
    "measurementId": "G-ZX713SES8G",
    "databaseURL": ""
}

pb = pyrebase.initialize_app(firebaseConfig)


def get_pb():
    return pb
