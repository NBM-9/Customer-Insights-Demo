# etl_demo.py

import pandas as pd
import numpy as np

# Step 1: Create fake customer data
data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Churned': [False, True, False, True, False],
    'TotalPurchases': [5, 2, 3, 1, 4]
}

df = pd.DataFrame(data)

# Step 2: Clean data - example: no missing values here, but let's say
df['TotalPurchases'] = df['TotalPurchases'].fillna(0)

# Step 3: Simple analysis - calculate churn rate
churn_rate = df['Churned'].mean()

print(f"Customer Data:\n{df}\n")
print(f"Churn Rate: {churn_rate:.2f}")

# Step 4: Save cleaned data to CSV (simulate ETL output)
df.to_csv('cleaned_customer_data.csv', index=False)
