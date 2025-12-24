-- Consultas Analíticas para Insights de Negócio

-- 1. Faturamento Total por Categoria de Produto
SELECT 
    p.category,
    SUM(f.total_amount) as total_revenue,
    SUM(f.quantity) as total_quantity
FROM fact_sales f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

-- 2. Evolução Mensal de Vendas (Faturamento)
SELECT 
    d.year,
    d.month,
    SUM(f.total_amount) as monthly_revenue
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 3. Top 5 Clientes por Volume de Compras
SELECT 
    c.customer_name,
    COUNT(f.transaction_id) as total_orders,
    SUM(f.total_amount) as total_spent
FROM fact_sales f
JOIN dim_customers c ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 5;

-- 4. Performance por Localização de Loja
SELECT 
    store_location,
    AVG(total_amount) as avg_ticket,
    SUM(total_amount) as total_revenue
FROM fact_sales f
GROUP BY store_location
ORDER BY total_revenue DESC;
