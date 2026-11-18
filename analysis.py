"""Sales Data Analysis - cleaning, analysis and charts with Pandas.
Put your Kaggle sales CSV in this folder as sales.csv, then edit the
column names below to match your file and run: python analysis.py
"""
import pandas as pd

# ---- 1. Edit these to match your CSV's column names ----
FILE = "sales.csv"
DATE, PRODUCT, REGION = "Order Date", "Item Type", "Region"
QTY, PRICE = "Units Sold", "Unit Price"

# ---- 2. Load and look at the data ----
df = pd.read_csv(FILE, encoding="latin-1")
print("Rows, columns:", df.shape)
print(df.head())
print(df.isnull().sum())

# ---- 3. Clean the data ----
df = df.drop_duplicates()
df = df.dropna(subset=[DATE, PRODUCT, QTY, PRICE])
df[DATE] = pd.to_datetime(df[DATE], errors="coerce")
df = df.dropna(subset=[DATE])
df["Revenue"] = df[QTY] * df[PRICE]
df["Month"] = df[DATE].dt.to_period("M").astype(str)
df.to_csv("sales_clean.csv", index=False)  # load this into MySQL for queries.sql

# ---- 4. Analyse ----
top_products = df.groupby(PRODUCT)["Revenue"].sum().sort_values(ascending=False).head(5)
monthly = df.groupby("Month")["Revenue"].sum()
print("\nTop 5 products by revenue:\n", top_products)
print("\nMonthly revenue:\n", monthly)
if REGION in df.columns:
    print("\nRevenue by region:\n", df.groupby(REGION)["Revenue"].sum())

# ---- 5. Charts: make them in Excel from sales_clean.csv ----
print("\nSaved sales_clean.csv - open it in Excel and insert a chart.")
