
CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  price NUMERIC,
  category_id INTEGER REFERENCES categories(id)
);

INSERT INTO categories (name) VALUES
('Baju'), ('Elektronik'), ('Otomotif');

INSERT INTO products (name, price, category_id) VALUES
('Baju HMIF', 135000, 1),
('Earphone Wireless', 150000, 2),
('Helm NJS', 500000, 3);
