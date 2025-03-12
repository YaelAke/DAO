from pymongo import MongoClient

def obtener_db():
    MONGO_URI = "mongodb+srv://al068350:p6RChkcjLh39QYln@cluster0.0bwry.mongodb.net/Chat?retryWrites=true&w=majority"
    cliente = MongoClient(MONGO_URI)
    return cliente["users_db"]
