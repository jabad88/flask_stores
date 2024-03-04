import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema


blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, message="Store not found.")
    
    
    def delete(store_id):
        try:
            del stores[store_id]
            return {"message":"Store deleted."}
        except KeyError:
            return abort(404, message="Store not found.")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return stores.values()


    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self,store_data):
        # store_data = request.get_json()
        # print(store_data)

        #ensure name key is in data
        if "name" not in store_data:
            abort (400, message="Bad request. Ensure 'name' is included in JSON payload. ")

        #check if store already exists
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store already exists")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id":store_id}
        stores[store_id] = store
        return store, 201