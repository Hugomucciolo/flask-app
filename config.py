from pymongo import MongoClient

client = MongoClient()
db = client['flask-app']