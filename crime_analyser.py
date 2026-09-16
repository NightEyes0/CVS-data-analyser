import pandas as pd

print("Loading crime data...")
data = pd.read_csv("crime_data.csv")

# 1. Show the original data length
print(f"Original row count: {len(data)}")

# 2. Clean the data (Drop any row that has a missing/NaN value)
clean_data = data.dropna()

# 3. Show the new data length
print(f"Cleaned row count: {len(clean_data)}")

print("\nCleaned Data Table:")
print(clean_data)