import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.police.uk/api/crimes-street/all-crime?lat=51.5074&lng=-0.1278"

print("Connecting to the UK Police API...")
response = requests.get(url)

if response.status_code == 200:
    print("Connection successful! Processing data...")
    raw_data = response.json()
    
    # --- NEW: Pandas Integration ---
    
    # 1. Convert the JSON list directly into a Pandas table (DataFrame)
    data = pd.DataFrame(raw_data)
    
    # 2. Count the crime categories (We use 'category' because that is the key in the JSON)
    crime_counts = data['category'].value_counts()
    
    # 3. Print the top 5 crimes
    print("\nTop 5 Crimes in Central London this month:")
    print(crime_counts.head(5))
    
    # 4. Generate the Chart
    print("\nGenerating live data chart...")
    crime_counts.plot(kind='bar', color='coral')
    plt.title("Central London Crime Reports (Live API)")
    plt.xlabel("Crime Category")
    plt.ylabel("Number of Reports")
    plt.tight_layout()
    plt.savefig("live_crime_chart.png")
    
    print("Chart saved as 'live_crime_chart.png'!")

else:
    print("Failed to connect to the API.")