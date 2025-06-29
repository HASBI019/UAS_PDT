
import redis

r = redis.Redis(host='redis', port=6379, db=0)

def get_stock(product_id):
    stock = r.get(f'stock:product:{product_id}')
    return int(stock) if stock else 0
