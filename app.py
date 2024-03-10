import os

from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] ="3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api=Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)

    return app

























# #GET all stores
# @app.get("/store")
# def get_stores():
#     return {"stores":list(stores.values())}


# #POST new store
# @app.post("/store") 
# #.post allows for post requests. post creates a new resource on server. basically submits data to server
# def create_store():
#     store_data = request.get_json()
#     print(store_data)

#     #ensure name key is in data
#     if "name" not in store_data: ### check against code from prof
#         abort (400, message="Bad request. Ensure 'name' is included in JSON payload. ")

#     ####check if store already exists
#     # for store in store_data:
#     #     if store["name"] in stores.values():
#     #         abort(400, message="Bad request. Store already exists") BAD CODE??? OR WAS IT?

#     #check if store already exists
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message="Store already exists")
    
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id":store_id}
#     stores[store_id] = store
#     return store, 201


# #GET single store id
# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         return abort(404, message="Store not found.")

# #DEL single store
# @app.delete("/item/<string:store_id>")
# def del_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message":"Store deleted."}
#     except KeyError:
#         return abort(404, message="Store not found.")


# #----------------ITEMS---------------------------#

# #GET single item id
# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         return abort(404, message="Item not found.")


# #DEL single item id
# @app.delete("/item/<string:item_id>")
# def del_item(item_id):
#     try:
#         del items[item_id]
#         return {"message":"Item deleted."}
#     except KeyError:
#         return abort(404, message="Item not found.")


# #GET all items
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}


# #POST new item
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     print(item_data)
    
#     #validate data exists and data type.
#     if ("price" not in item_data 
#     or "store_id" not in item_data 
#     or "name" not in item_data): #later, validate that the type of data is correct type. Price should be float.
#         abort(400, message="Bad request. Ensure 'price', 'store_id', 'name' are included in the JSON payload.")

#     ###validate item and store_id is not in item_data twice.
#     for item in items.values():
#         if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
#             abort(400, message="Item already exists")

#     #validate store_id is in the dictionary of stores in db.
#     if item_data["store_id"] not in stores:
#         return abort(404, message="Store not found.")
    
#     item_id = uuid.uuid4().hex
#     new_item = {**item_data, "id":item_id} #adding item id in "id":item_id
#     print(new_item)
#     items[item_id] = new_item
#     return new_item, 201


# #UPDATE single item
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     print(item_data)

#     #validate "price" and "name" are in item_data JSON
#     if "price" not in item_data or "name" not in item_data:
#         return abort(400, message="Bad request. Ensure 'price' and 'name' are included in JSON payload.")

#     try:
#         item = items[item_id]
#         print(item)
#         item |= item_data #update dictionary is used with |=
#         print(item)

#         return item
#     except KeyError:
#         abort(404, message="Item not found")
