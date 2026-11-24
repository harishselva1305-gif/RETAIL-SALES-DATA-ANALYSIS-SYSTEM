
import pandas as pd
import os

# ==========================================
# PROJECT: RETAIL SALES DATA ANALYSIS
# TECHNOLOGY: PYTHON PANDAS
# ==========================================

# Create folders
os.makedirs("datasets", exist_ok=True)
os.makedirs("output", exist_ok=True)

print("=" * 60)
print("       RETAIL SALES DATA ANALYSIS SYSTEM")
print("=" * 60)


# ==========================================
# 1. SERIES AND DATAFRAMES
# ==========================================

print("\n1. CREATING PANDAS SERIES AND DATAFRAMES")

product_prices = pd.Series([500, 1200, 800, 1500])

print("\nProduct Prices Series:")
print(product_prices)

sales_data = {
    "Order_ID": [101, 102, 103, 104, 105, 106,
                 107, 108, 109, 110],
    "Customer_ID": [1, 2, 3, 1, 4, 5, 2, 3, 6, 4],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop",
                "Monitor", "Mouse", "Keyboard", "Laptop",
                "Monitor", "Mouse"],
    "Category": ["Electronics", "Accessories", "Accessories",
                 "Electronics", "Electronics", "Accessories",
                 "Accessories", "Electronics", "Electronics",
                 "Accessories"],
    "Quantity": [2, 5, 3, 1, 2, 4, 2, 1, 3, 6],
    "Price": [50000, 500, 1200, 50000, 15000,
              500, 1200, 50000, 15000, 500],
    "Order_Date": [
        "2026-01-05", "2026-01-10", "2026-02-12",
        "2026-02-15", "2026-03-01", "2026-03-10",
        "2026-04-05", "2026-04-15", "2026-05-10",
        "2026-05-20"
    ]
}

sales_df = pd.DataFrame(sales_data)

customers_data = {
    "Customer_ID": [1, 2, 3, 4, 5, 6],
    "Customer_Name": ["Arun", "Priya", "Kumar",
                      "Divya", "Rahul", "Sneha"],
    "City": ["Chennai", "Bangalore", "Chennai",
             "Coimbatore", "Madurai", "Bangalore"]
}

customers_df = pd.DataFrame(customers_data)


# ==========================================
# 2. SAVE DATASETS
# ==========================================

print("\n2. CREATING SAMPLE DATASETS")

sales_df.to_csv("datasets/sales.csv", index=False)

customers_df.to_excel(
    "datasets/customers.xlsx",
    index=False
)

print("Sales CSV created successfully!")
print("Customer Excel file created successfully!")


# ==========================================
# 3. READING CSV AND EXCEL FILES
# ==========================================

print("\n3. READING DATASETS")

sales = pd.read_csv("datasets/sales.csv")

customers = pd.read_excel("datasets/customers.xlsx")

print("\nSales Dataset:")
print(sales.head())

print("\nCustomer Dataset:")
print(customers.head())


# ==========================================
# 4. SELECTING DATA USING LOC AND ILOC
# ==========================================

print("\n4. SELECTING DATA")

# Select rows using loc
print("\nLOC - First three records:")
print(sales.loc[0:2, ["Product", "Quantity", "Price"]])

# Select rows using iloc
print("\nILOC - First three rows and columns:")
print(sales.iloc[0:3, 0:4])


# ==========================================
# 5. FILTERING AND SORTING
# ==========================================

print("\n5. FILTERING AND SORTING")

# Filter expensive products
expensive_products = sales[sales["Price"] > 10000]

print("\nProducts above Rs. 10,000:")
print(expensive_products)

# Filter electronics
electronics = sales[sales["Category"] == "Electronics"]

print("\nElectronics Sales:")
print(electronics)

# Sort sales by quantity
sorted_sales = sales.sort_values(
    by="Quantity",
    ascending=False
)

print("\nSales Sorted by Quantity:")
print(sorted_sales)


# ==========================================
# 6. APPLYING FUNCTIONS TO DATA
# ==========================================

print("\n6. APPLYING FUNCTIONS")

# Calculate total sales
sales["Revenue"] = (
    sales["Quantity"] * sales["Price"]
)

# Apply 10% discount for orders above Rs. 50,000
def calculate_discount(revenue):
    if revenue > 50000:
        return revenue * 0.10
    return 0

sales["Discount"] = sales["Revenue"].apply(
    calculate_discount
)

# Calculate final revenue
sales["Final_Revenue"] = (
    sales["Revenue"] - sales["Discount"]
)

print("\nRevenue Calculation:")
print(sales[
    ["Product", "Revenue", "Discount", "Final_Revenue"]
])


# ==========================================
# 7. GROUPING AND AGGREGATION
# ==========================================

print("\n7. GROUPBY AND AGGREGATION")

# Category-wise sales
category_sales = sales.groupby("Category").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Final_Revenue", "sum"),
    Average_Revenue=("Final_Revenue", "mean")
)

print("\nCategory-wise Sales:")
print(category_sales)

# Product-wise sales
product_sales = sales.groupby("Product")[
    "Final_Revenue"
].sum().sort_values(ascending=False)

print("\nProduct-wise Revenue:")
print(product_sales)


# ==========================================
# 8. MERGING AND JOINING
# ==========================================

print("\n8. MERGING AND JOINING")

# Merge sales and customer datasets
merged_data = pd.merge(
    sales,
    customers,
    on="Customer_ID",
    how="inner"
)

print("\nMerged Sales and Customer Data:")
print(merged_data[
    ["Order_ID", "Customer_Name", "City",
     "Product", "Final_Revenue"]
])

# Find city-wise sales
city_sales = merged_data.groupby("City")[
    "Final_Revenue"
].sum().sort_values(ascending=False)

print("\nCity-wise Revenue:")
print(city_sales)


# ==========================================
# 9. PIVOT TABLES
# ==========================================

print("\n9. PIVOT TABLE ANALYSIS")

pivot_table = pd.pivot_table(
    merged_data,
    values="Final_Revenue",
    index="Category",
    columns="City",
    aggfunc="sum",
    fill_value=0
)

print("\nCategory and City Pivot Table:")
print(pivot_table)


# ==========================================
# 10. WORKING WITH DATES
# ==========================================

print("\n10. DATE ANALYSIS")

sales["Order_Date"] = pd.to_datetime(
    sales["Order_Date"]
)

# Extract year, month and day
sales["Year"] = sales["Order_Date"].dt.year
sales["Month"] = sales["Order_Date"].dt.month
sales["Month_Name"] = sales["Order_Date"].dt.month_name()
sales["Day"] = sales["Order_Date"].dt.day

# Monthly revenue analysis
monthly_sales = sales.groupby(
    ["Year", "Month", "Month_Name"]
)["Final_Revenue"].sum().reset_index()

print("\nMonthly Sales:")
print(monthly_sales)

# Find latest order
latest_order = sales["Order_Date"].max()

print("\nLatest Order Date:", latest_order)


# ==========================================
# 11. TOP CUSTOMERS
# ==========================================

print("\n11. TOP CUSTOMER ANALYSIS")

customer_sales = merged_data.groupby(
    ["Customer_ID", "Customer_Name"]
)["Final_Revenue"].sum().sort_values(
    ascending=False
)

print("\nTop Customers:")
print(customer_sales)


# ==========================================
# 12. BUSINESS INSIGHTS
# ==========================================

print("\n12. BUSINESS INSIGHTS")

total_revenue = sales["Final_Revenue"].sum()

total_orders = sales["Order_ID"].nunique()

best_product = product_sales.idxmax()

best_category = category_sales[
    "Total_Revenue"
].idxmax()

best_city = city_sales.idxmax()

print("\nTotal Revenue: Rs.", total_revenue)
print("Total Orders:", total_orders)
print("Best Selling Product by Revenue:", best_product)
print("Best Performing Category:", best_category)
print("Highest Revenue City:", best_city)


# ==========================================
# 13. EXPORT ANALYSIS RESULTS
# ==========================================

print("\n13. EXPORTING RESULTS")

sales.to_csv(
    "output/cleaned_sales.csv",
    index=False
)

category_sales.to_csv(
    "output/category_sales.csv"
)

monthly_sales.to_csv(
    "output/monthly_sales.csv",
    index=False
)

pivot_table.to_excel(
    "output/sales_pivot.xlsx"
)

print("\nAll reports exported successfully!")


# ==========================================
# PROJECT COMPLETED
# ==========================================

print("\n" + "=" * 60)
print("       RETAIL SALES ANALYSIS COMPLETED")
print("=" * 60)
