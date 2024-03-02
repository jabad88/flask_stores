from flask import Flask, request
from db import stores, items

app = Flask(__name__)



@app.route("/store")
def store_name():
    return {"stores":stores}

@app.post("/store") #.post allows for post requests. post creates a new resource on server. basically submits data to server
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            # return store["item"], 200 #different code from e-book. prof. says this is fine, but a dictionary object is better because if you need to make changes in the future, your code will already be set up with returning the full object and not a list. Correct code below
            return {"items": store["items"]}
    return {"message":"Store not found"}, 404