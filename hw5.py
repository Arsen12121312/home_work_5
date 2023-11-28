CREATE DATABASE myDatabase;
USE myDatabase;

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO categories (name) VALUES ('Electronics'), ('Books'), ('Toys');

INSERT INTO products (name, price, category_id) VALUES ('Laptop', 800.00, 1), ('Smartphone', 600.00, 1), ('Book1', 10.00, 2), ('Book2', 15.00, 2), ('Toy Car', 20.00, 3);

SELECT * FROM products WHERE category_id = <id>;