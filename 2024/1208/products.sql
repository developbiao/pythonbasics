-- CREATE products database
CREATE DATABASE products;


-- Create the products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);


-- Insert the product data
INSERT INTO products (name, price) VALUES
    ('Widget', 19.99),
    ('Gadget', 29.99),
    ('Gizmo', 39.99),
    ('Smart Watch', 199.99),
    ('Wireless Earbuds', 89.99),
    ('Portable Charger', 24.99),
    ('Bluetooth Speaker', 79.99),
    ('Phone Stand', 15.99),
    ('Laptop Sleeve', 34.99),
    ('Mini Drone', 299.99),
    ('LED Desk Lamp', 45.99),
    ('Keyboard', 129.99),
    ('Mouse Pad', 12.99),
    ('USB Hub', 49.99),
    ('Webcam', 69.99),
    ('Screen Protector', 9.99),
    ('Travel Adapter', 27.99),
    ('Gaming Headset', 159.99),
    ('Fitness Tracker', 119.99),
    ('Portable SSD', 179.99);
