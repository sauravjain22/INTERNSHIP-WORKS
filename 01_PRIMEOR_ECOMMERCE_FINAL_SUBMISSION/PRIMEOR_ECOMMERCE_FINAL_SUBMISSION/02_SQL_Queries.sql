-- Primeor Ecommerce Analytics
-- Level 2 - SQL Analysis
-- Task 2

-- 1. Top 10 profitable products
SELECT
    product_name,
    SUM(profit) AS total_profit
FROM ecommerce_sales
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;


-- 2. Top 10 customers by sales
SELECT
    customer_name,
    SUM(sales) AS total_sales
FROM ecommerce_sales
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- 3. Region-wise total sales
SELECT
    region,
    SUM(sales) AS total_sales
FROM ecommerce_sales
GROUP BY region
ORDER BY total_sales DESC;


-- 4. Category-wise average profit
SELECT
    category,
    AVG(profit) AS average_profit
FROM ecommerce_sales
GROUP BY category
ORDER BY average_profit DESC;


-- 5. Category with the highest average discount
SELECT
    category,
    AVG(discount) AS average_discount
FROM ecommerce_sales
GROUP BY category
ORDER BY average_discount DESC
LIMIT 1;


-- 6. Orders with negative profit
SELECT
    order_id,
    order_date,
    customer_name,
    product_name,
    sales,
    profit
FROM ecommerce_sales
WHERE profit < 0
ORDER BY profit ASC;


-- 7. Monthly sales trend
SELECT
    DATE_TRUNC('month', order_date) AS sales_month,
    SUM(sales) AS total_sales
FROM ecommerce_sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month ASC;


-- 8. Market-wise revenue analysis
SELECT
    market,
    SUM(sales) AS total_revenue
FROM ecommerce_sales
GROUP BY market
ORDER BY total_revenue DESC;


-- 9. Top-performing sub-categories
SELECT
    sub_category,
    SUM(profit) AS total_profit
FROM ecommerce_sales
GROUP BY sub_category
ORDER BY total_profit DESC
LIMIT 10;


-- 10. Ship mode usage
SELECT
    x AS ship_mode,
    COUNT(*) AS usage_count
FROM ecommerce_sales
GROUP BY x
ORDER BY usage_count DESC;
