from flask import Flask, jsonify
from db_postgres import get_all_products
from db_redis import get_stock
from db_mongo import get_metadata  # pastikan file db_mongo.py sudah ada

app = Flask(__name__)

@app.route('/products')
def products():
    items = get_all_products()  # data dari PostgreSQL
    for item in items:
        item['stock'] = get_stock(item['id'])  # stok dari Redis
        metadata = get_metadata(item['id'])    # deskripsi & review dari MongoDB
        item['description'] = metadata['description']
        item['reviews'] = metadata['reviews']
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
