import pandas as pd

print("Loading and cleaning crime data...")
data = pd.read_csv("crime_data.csv")
clean_data = data.dropna()

print("\n--- Crime Analysis ---")
# Focus on just the 'Crime_type' column and count the occurrences
crime_counts = clean_data['Crime_type'].value_counts()

print("Most frequent crimes:")
print(crime_counts)