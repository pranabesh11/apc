import pymongo

if __name__ =="__main__":
    print("hello pranabesh")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["pranabesh"]
    collection = db['mysamplecollectionforpranabesh']
    mydict = { "name": "John", "address": "Highway 37" }
    collection.insert_one(mydict)