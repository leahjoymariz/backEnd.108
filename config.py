import pymongo
import certifi

con_str = "mongodb+srv://leahjoymariz:test1234@cluster0.hhdbaa9.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore")