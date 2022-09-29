import pymongo

client = pymongo.MongoClient("mongodb+srv://Mosharrafa:HDj3xJJLwH235jCzQ@cluster0.dbzzgfx.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)

d = {
    "name": "Italy",
    "email":"abc@gmail.com",
    "surname": "Germany"
}

db1= client['mongotest']
coll=db1['test']
coll.insert_one(d)