import sqlite3
import pandas as pd
from pathlib import Path

# Project folders
base = Path(__file__).parent
db_path = base / "database" / "ecommerce.db"
output = base / "data" / "processed"

# Connect to database
conn = sqlite3.connect(db_path)

# SQL analyses
queries = {
    "kpis": """
        SELECT
            COUNT(*) AS total_orders,
            ROUND(SUM(sales), 2) AS total_sales,
            ROUND(SUM(profit), 2) AS total_profit,
            ROUND(AVG(sales), 2) AS avg_sales_per_order
        FROM ecommerce_sales
    """,
    "category": """
        SELECT category,
               COUNT(*) AS order_count,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM ecommerce_sales
        GROUP BY category
        ORDER BY total_sales DESC
    """,
    "city": """
        SELECT city,
               COUNT(*) AS order_count,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM ecommerce_sales
        GROUP BY city
        ORDER BY total_sales DESC
    """,
    "monthly": """
        SELECT strftime('%Y-%m', order_date) AS month,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit,
               COUNT(*) AS order_count
        FROM ecommerce_sales
        GROUP BY strftime('%Y-%m', order_date)
        ORDER BY month
    """,
    "customers": """
        SELECT customer_segment,
               COUNT(*) AS order_count,
               COUNT(DISTINCT customer_id) AS unique_customers,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM ecommerce_sales
        GROUP BY customer_segment
        ORDER BY total_sales DESC
    """,
    "status": """
        SELECT order_status,
               COUNT(*) AS order_count,
               ROUND(SUM(sales), 2) AS total_sales,
               ROUND(SUM(profit), 2) AS total_profit
        FROM ecommerce_sales
        GROUP BY order_status
        ORDER BY order_count DESC
    """
}

# Run queries and export results
for name, query in queries.items():
    result = pd.read_sql_query(query, conn)
    result.to_csv(output / f"{name}.csv", index=False)
    print(f"{name}.csv saved ({len(result)} rows)")

conn.close()
print("All SQL analyses completed!")