-- Base de données : shop

CREATE DATABASE IF NOT EXISTS shop;
USE shop;


------------------------
-- Table dim produit
------------------------

CREATE TABLE IF NOT EXISTS dim_poduct (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL UNIQUE,
    cateogry VARCHAR(50),
    price DECIMAL(10,2)
);

-----------------------
--Table dimension date
-----------------------

CREATE TABLE IF NOT EXISTS dim_date (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    year INT,
    week INT
);

----------------------
-- Table fact_sales
----------------------

CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    data_id DATE NOT NULL,
    quantity INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (product_id) REFERENCES dim_poduct(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(data_id)
);

------------------------------------
-- Index pour accélerer les requetes
------------------------------------

CREATE INDEX idx_fact_product ON fact_sales(product_id);
CREATE INDEX idx_fac_date ON fact_sales(data_id);
