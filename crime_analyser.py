import pandas as pd
import matplotlib.pyplot as plt

print("Loading and cleaning crime data...")
data = pd.read_csv("crime_data.csv")
clean_data = data.dropna()

print("\n--- Crime Analysis ---")
crime_counts = clean_data['Crime_type'].value_counts()
print("Most frequent crimes:")
print(crime_counts)

# --- NEW: Data Visualisation ---
print("\nGenerating crime chart...")

# Create a bar chart using our counted data
crime_counts.plot(kind='bar', color='skyblue')

# Add titles and labels so people know what they are looking at
plt.title("Most Common Crimes")
plt.xlabel("Crime Type")
plt.ylabel("Number of Reports")

# This ensures the text at the bottom doesn't get cut off
plt.tight_layout()

# Save the chart as an image file in our folder
plt.savefig("crime_chart.png")

print("Chart successfully saved as 'crime_chart.png'!")