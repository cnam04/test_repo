from pathlib import Path

import pandas as pd
import time


sales = pd.read_csv(Path(__file__).with_name("sales.csv"))
sales["revenue"] = sales["units_sold"] * sales["unit_price"]
print(f"Analyzed {len(sales)} sales records")
print(f"Total revenue: ${sales['revenue'].sum():.2f}")
print(f"Average revenue per record: ${sales['revenue'].mean():.2f}")
print(f"Highest-revenue product: {sales.loc[sales['revenue'].idxmax(), 'product']}")

for i in range(10):
    print(f"Wait number: {i}")
    time.sleep(1.5)