import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items",__name__, description = "Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    
    #GET single item
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        try:
            return items[item_id]
        except KeyError:
            return abort(404, message="Item not found.")
    
    #DELETE single item
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message":"Item deleted."}
        except KeyError:
            return abort(404, message="Item not found.")

    #UPDATE single item
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)
    def put(self,item_data, item_id):
        # item_data = request.get_json()
        # print(item_data)

        # #validate "price" and "name" are in item_data JSON
        # if "price" not in item_data or "name" not in item_data:
        #     return abort(400, message="Bad request. Ensure 'price' and 'name' are included in JSON payload.")

        try:
            item = items[item_id]
            print(item)
            item |= item_data #update dictionary is used with |=
            print(item_data)

            return item
        except KeyError:
            abort(404, message="Item not found")


@blp.route("/item")
class ItemList(MethodView):
    
    #get list of items
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return items.values()


    @blp.arguments(ItemSchema)
    @blp.response(201,ItemSchema)
    def post(self,item_data):
        # item_data = request.get_json()
        # print(item_data)
        
        ##COMMENTED OUT BECAUSE MARSHMALLOW
        # #validate data exists and data type.
        # if ("price" not in item_data 
        # or "store_id" not in item_data 
        # or "name" not in item_data): #later, validate that the type of data is correct type. Price should be float.
        #     abort(400, message="Bad request. Ensure 'price', 'store_id', 'name' are included in the JSON payload.")

        #validate item and store_id is not in item_data twice.
        for item in items.values():
            if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
                abort(400, message="Item already exists")

        #validate store_id is in the dictionary of stores in db.
        # if item_data["store_id"] not in stores:
        #     return abort(404, message="Store not found.")
        
        item_id = uuid.uuid4().hex
        new_item = {**item_data, "id":item_id} #adding item id in "id":item_id
        print(new_item)
        items[item_id] = new_item
        return new_item, 201
