from pathlib import Path

import pandas as pd
import random
import time


sales = pd.read_csv(Path(__file__).with_name("sales.csv"))
sales["revenue"] = sales["units_sold"] * sales["unit_price"]
print(f"Analyzed {len(sales)} sales records")
print(f"Total revenue: ${sales['revenue'].sum():.2f}")
print(f"Average revenue per record: ${sales['revenue'].mean():.2f}")
print(f"Highest-revenue product: {sales.loc[sales['revenue'].idxmax(), 'product']}")

analysis_duration = random.uniform(5, 15)
log_messages = [
    "Loading sales segments",
    "Validating transaction records",
    "Calculating revenue trends",
    "Comparing product performance",
    "Preparing summary metrics",
]
deadline = time.monotonic() + analysis_duration

print(f"Running extended analysis for {analysis_duration:.1f} seconds")
while True:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        break

    time.sleep(min(random.uniform(0.5, 2.0), remaining))
    print(f"{random.choice(log_messages)}...")

print("Extended analysis complete")