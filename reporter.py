
import os
import pandas as pd


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

csv_filename = "sales-201710.csv"

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)
    
sales = pd.read_csv(csv_filepath) 

monthly_total = sales["sales price"].sum()
product_totals = sales.groupby(["product"]).sum()
product_totals = product_totals.sort_values("sales price", ascending=False)
top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1



print("-------------------------")
month = "NOVEMBER" 
year = 2017 
print(f"SALES REPORT","(", f"DATE: {month} {year}", ")")
print("-------------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")
print("-------------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))

# reference a file in the "data" directory
# ... adapted from: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md#file-operations
# read csv file into a pandas dataframe object
# ... this and other pandas operations adapted from: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/pandas.md
# google search for "pandas group by" leads to...
# ... https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

# google search for "pandas dataframe order rows" leads to ...
# ... http://pandas.pydata.org/pandas-docs/version/0.19/generated/pandas.DataFrame.sort.html

# google search for "pandas loop through each row in a dataframe" results in ...
# ... https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
# ... http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html
