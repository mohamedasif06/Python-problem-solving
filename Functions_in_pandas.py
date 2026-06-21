# analyzer.py-----------------------------
import pandas as pd
from helpers import calculate_total, format_currency

df = pd.read_csv('output/sales_data.csv')
print(df)
totals=[]
for index,rows in df.iterrows():
    total = calculate_total(rows['quantity'],rows['price'])
    totals.append(total)

df['totals'] = totals
print('\n')
print("Sales data:")
for index,rows in df.iterrows():
    formatted = format_currency(rows['totals'])
    print(f"{rows['product']}:{formatted}") 

print(f"\n{df}")

# helpers.py-------------------------------------------
def calculate_total(quantity,price):
    return quantity*price

def format_currency(amount):
    return f"${amount:,.2f}"
