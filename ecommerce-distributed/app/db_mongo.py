from pymongo import MongoClient

# Koneksi ke MongoDB container (service name: mongodb, lihat di docker-compose)
client = MongoClient("mongodb://mongodb:27017/")
db = client["ecommerce"]
collection = db["product_metadata"]

def get_metadata(product_id):
    result = collection.find_one({"product_id": product_id})
    if result:
        return {
            "description": result.get("description", ""),
            "reviews": result.get("reviews", [])
        }
    return {"description": "", "reviews": []}
