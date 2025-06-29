
import psycopg2

def get_all_products():
    conn = psycopg2.connect(
        dbname="ecommerce", user="user", password="password", host="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "price": float(r[2])} for r in rows]
