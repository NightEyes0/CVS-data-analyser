import pandas as pd

print("Loading crime data...")

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv("crime_data.csv")

# Print the table /output
print(data)