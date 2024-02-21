from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import mongodb_collection
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

import os

class NoSQL():

    uri = os.getenv('MONGODB_URL')

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    db = client.asset_db

    asset_collection = db[mongodb_collection]

    # Send a ping to confirm a successful connection
    try:
        
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)