from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

from pymongo import MongoClient

client = MongoClient('mongo', 27017)

db = client.test_database
collection = db.test_collection

@app.get("/{fruit}")
def add_list_fruits(fruit):
    id = collection.insert_one({"fruit": fruit}).inserted_id
    return list(collection.find({}, {"_id": False}))


