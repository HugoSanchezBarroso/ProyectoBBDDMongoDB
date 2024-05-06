import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.oop_languages
mycol = db["language"]

myquery = { "Nombre": "Java"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

db.language.insert_one({"_id": 11, "Nombre": "Simula", "Herencia": "true", "Multiplataforma": "false", "Polimorfismo": "true", "Encapsulamiento": "true"})

myquery = { "Nombre": "Simula"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)