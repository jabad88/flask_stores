from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id =fields.Str(dump_only=True) #dump_only = field will not be used OR expected. When we serialize data to be returned to the client, the id field will be included in that output.
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    

class ItemUpdateSchema(Schema):
    name = fields.Str() #these schemas will only be used for incoming data. we don't want a user changing store_id.
    price = fields.Float()

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)