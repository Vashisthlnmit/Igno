from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
db_stri=os.getenv("MONGO_DB")
db_name=os.getenv("DB_NAME")
client=MongoClient(db_stri,server_api=ServerApi('1'))
db=client.get_database(db_name)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)