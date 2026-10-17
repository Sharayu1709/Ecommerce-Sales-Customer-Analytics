-- 1. Overall sales and profit
SELECT
    COUNT(*) AS total_orders,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(AVG(sales), 2) AS avg_sales_per_order
FROM ecommerce_sales;

-- 2. Sales and profit by category
SELECT
    category,
    COUNT(*) AS order_count,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Sales and profit by city
SELECT
    city,
    COUNT(*) AS order_count,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY city
ORDER BY total_sales DESC;

-- 4. Monthly sales and profit
SELECT
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    COUNT(*) AS order_count
FROM ecommerce_sales
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month;

-- 5. Sales by customer segment
SELECT
    customer_segment,
    COUNT(*) AS order_count,
    COUNT(DISTINCT customer_id) AS unique_customers,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY customer_segment
ORDER BY total_sales DESC;

-- 6. Orders by status
SELECT
    order_status,
    COUNT(*) AS order_count,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM ecommerce_sales
GROUP BY order_status
ORDER BY order_count DESC;