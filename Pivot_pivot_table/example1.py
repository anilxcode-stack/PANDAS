""" Real-World Example: E-Commerce Sales Analysis """

"""
📊 Problem Statement:

You have sales data of an online store.
You want to analyze:

Total sales per region
Sales distribution across product categories
Monthly performance
"""

import pandas as pd

# Step1: Create realistic dataset

data = {
    "Order_ID" : [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Regin": ["North","South","East","West","North","South","East","West","North","South"],
    "Category": ["Electronics","Clothing","Electronics","Furniture","Clothing",
                 "Furniture","Clothing","Electronics","Furniture","Clothing"],
    "Sales": [20000, 15000, 18000, 22000, 12000, 25000, 14000, 21000, 23000, 16000],
    "Month": ["Jan","Jan","Feb","Feb","Mar","Mar","Apr","Apr","May","May"]
}
df = pd.DataFrame(data)

print("Original Data:\n", df)

# Step 2: Total Sales per Region

pivot1 = pd.pivot_table(df,
                        index = "Regin",
                        values="Sales",
                        aggfunc="sum")

# print("\nTotal Sales per Regin:\n", pivot1)

# Step 3 :  Region vs Category Sales 

pivot2 = pd.pivot_table(df, 
                        index ="Regin",
                        columns="Category",
                        values="Sales",
                        aggfunc="sum",
                        fill_value=0)

# print("\nSales by Region and Category:\n", pivot2)

# Step 4: Monthly Sales Trend

pivot3 = pd.pivot_table(df,
                        index="Month",
                        values="Sales",
                        aggfunc="sum")
print("\nMonthly Sales Trend:\n", pivot3)