import json
import pymongo

mongo_host = "mongodb://root:P#ssw0rd@pyb-mongodb:27017/"
client = pymongo.MongoClient(mongo_host)
db = client["line_api_db"]
db_col = db["messages"]

# load the sample message
with open('./message.json', 'r', encoding='utf-8') as msg_file:
    message_data = json.load(msg_file)

# insert into collection
def insert_to_col(data):
    try:
        db_col.insert_one(data)
    except:
        print('Error')

# find the fist doc
def find_first_doc():
    doc = db_col.find_one()
    return doc

# find all or selection doc
def find_doc(query: dict=None, selection: dict=None):
    if query != None:
        for col in db_col.find(query, selection):
            return col

    for col in db_col.find():
        return col

selection = {"events": 1}
query = {"destination": "image_dest"}
print(find_doc(query=query, selection=selection))

