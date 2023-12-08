from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib as jb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

from pymongo import MongoClient

client = MongoClient('mongo', 27017)

db = client.test_database
collection = db.test_collection

""" @app.get("/{fruit}")
def add_list_fruits(fruit):
    id = collection.insert_one({"fruit": fruit}).inserted_id
    return list(collection.find({}, {"_id": False})) """

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

import pandas as pd

fichier_pkl = "./model.pkl"
model = jb.load(fichier_pkl)


Item.sepal_length=0.1
Item.sepal_width=0.1
Item.petal_length=0.1
Item.petal_width=0.1

@app.post("/predict")
def predict(item: Item):
    #item_data = jsonable_encoder(item)
    item_data = [item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]
    pred=model.predict([item_data])
    print(pred)
    return {"prediction": pred[0]}
