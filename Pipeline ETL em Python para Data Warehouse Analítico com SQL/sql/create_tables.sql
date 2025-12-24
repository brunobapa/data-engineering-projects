-- Script de Criação de Tabelas (DDL) para o Data Warehouse
-- Modelo: Star Schema (Esquema Estrela)

-- Dimensão de Produtos
CREATE TABLE IF NOT EXISTS dim_products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT
);

-- Dimensão de Clientes
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL
);

-- Dimensão de Tempo
CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE,
    day INTEGER,
    month INTEGER,
    year INTEGER,
    quarter INTEGER,
    day_of_week INTEGER
);

-- Tabela Fato de Vendas
CREATE TABLE IF NOT EXISTS fact_sales (
    transaction_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    date_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    total_amount REAL,
    store_location TEXT,
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
