""" Mini Project: Sales Performance Dashboard (Using pandas Pivot Table) """

"""
🎯 Objective

Analyze sales data to extract:

Region-wise performance
Category-wise contribution
Monthly trends
Top-performing segments
"""

import pandas as pd

# Step1: Create realistic dataset

data = {
    "Order_ID" : range(101, 121),
    "Region":["North", "South", "East", "West"] * 5,
    "Category": ["Electronics", "Clothing", "Furniture", "Electronics", "Clothing"] * 4,
    "Sales":[20000,15000,18000,22000,12000,
              25000,14000,21000,23000,16000,
              27000,19000,20000,24000,17000,
              26000,18000,22000,25000,21000],
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar"] * 4        
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

# Step 2: Region-wise total sales

region_sales = pd.pivot_table(df,
                              index="Region",
                              values="Sales",
                              aggfunc="sum")

# print("\nRegion-wise Sales:\n", region_sales)

# Step 3: Category-wise performance

category_sales = pd.pivot_table(df,
                                index="Category",
                                values="Sales",
                                aggfunc="sum")

# print("\nCategory-wise Sales:\n", category_sales)

# Step 4: Region vs Category (IMPORTANT)

region_category = pd.pivot_table(df,
                                 index="Region",
                                 columns="Category",
                                 values="Sales",
                                 aggfunc="sum",
                                 fill_value=0)
# print("\nRegion vs Categry:\n", region_category)

# step 5: Monthly trend analysis
monthly_sales = pd.pivot_table(df,
                               index="Month",
                               values="Sales",
                               aggfunc="sum")

# print("\nMonthly Sales Trend:\n", monthly_sales)

# Step 6 : Advanced (Multiple Aggregation)

advanced = pd.pivot_table(df,
                          index=["Region", "Category"],
                          values="Sales",
                          aggfunc=["sum", "mean", "max"]
                          )

print("\nAdvanced Analysis:\n", advanced)