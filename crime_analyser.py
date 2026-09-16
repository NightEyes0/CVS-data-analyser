import requests
import pandas as pd
import matplotlib.pyplot as plt

# We are using the GPS coordinates for Central London
url = "https://data.police.uk/api/crimes-street/all-crime?lat=51.5074&lng=-0.1278"

print("Connecting to the UK Police API...")
response = requests.get(url)

# A status code of 200 means "OK / Successful" in web development
if response.status_code == 200:
    print("Connection successful! Downloading live data...")
    
    # The API sends data back in JSON format, which Python converts to a list
    raw_data = response.json()
    
    print(f"Downloaded {len(raw_data)} recent crime reports!")
    
    # Let's print out just the very first crime report to see what the database gave us
    print("\nSample of the first crime report:")
    print(raw_data[0])
    
else:
    print(f"Failed to connect. Error code: {response.status_code}")