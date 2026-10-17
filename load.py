import pandas as pd
import sqlite3

# Read the processed dataset
df = pd.read_csv("data/processed/ecommerce_sales.csv")

# Create the SQLite database
conn = sqlite3.connect("database/ecommerce.db")

# Load the CSV data into a SQL table
df.to_sql("ecommerce_sales", conn, if_exists="replace", index=False)

print("Data loaded into SQLite successfully!")
print("Rows loaded:", len(df))

conn.close()