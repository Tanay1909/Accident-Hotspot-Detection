import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load the dataset (Replace with actual file path)
file_path = "traffic_accidents_india.csv"
df = pd.read_csv(file_path)

# Display basic info
print(df.head())
print(df.info())

# Convert Time_of_Day to categories
time_categories = ["Early Morning", "Morning", "Afternoon", "Evening", "Night", "Late Night"]
df["Time_of_Day"] = pd.Categorical(df["Time_of_Day"], categories=time_categories, ordered=True)

# --- 1. Accidents by Time of Day ---
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="Time_of_Day", order=time_categories, palette="coolwarm")
plt.title("Accidents by Time of Day in India")
plt.xlabel("Time of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.show()

# --- 2. Accidents by Weather Condition ---
plt.figure(figsize=(12, 5))
sns.countplot(data=df, x="Weather_Condition", palette="viridis")
plt.title("Accidents by Weather Condition in India")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.show()

# --- 3. Heatmap of Accident Hotspots ---
# Ensure we have valid coordinates
df = df.dropna(subset=["Latitude", "Longitude"])

# Create a base map centered at India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add heatmap
heat_data = list(zip(df["Latitude"], df["Longitude"]))
HeatMap(heat_data).add_to(m)

# Save map to file
m.save("accident_hotspots_india.html")

print("Heatmap saved as accident_hotspots_india.html. Open it in a browser to view the accident hotspots.")
