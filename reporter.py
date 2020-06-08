import operator
import pandas 

csv_filepath = "data/sales-201710.csv"
df = pandas.read_csv(csv_filepath)
print(type(df))
print(df.head())

sales-201710 = df.to_dict("records")


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

print("GENERATING SALES REPORT FOR MONTH OF OCTOBER 2013...")