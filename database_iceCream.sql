CREATE DATABASE IceCreamShop;

-- Use the Database
USE IceCreamShop;

-- Table for Ice Cream Flavors
CREATE TABLE IceCreamFlavors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flavor_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Table for Toppings
CREATE TABLE Toppings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    topping_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Table for Milkshakes
CREATE TABLE Milkshakes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flavor_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Table for Ice Cream Cakes
CREATE TABLE IceCreamCakes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flavor_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Table for Orders
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_mobile VARCHAR(15) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for Order Items (related to Orders)
CREATE TABLE OrderItems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_type VARCHAR(50), -- Ice Cream, Milkshake, Cake
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES Orders(id)
);
