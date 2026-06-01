import pandas as pd
import matplotlib
matplotlib.use('Agg')   # 🔥 FIX for graph crash
import matplotlib.pyplot as plt
import folium

print("Starting program...")

# Load dataset
data = pd.read_csv("sales_location_data.csv")

print("Data loaded successfully!")

# Graph
plt.figure(figsize=(10,5))
plt.bar(data["Region"], data["Sales"])
plt.xticks(rotation=45)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.savefig("graph.png")  # save graph
print("Graph saved!")

print("Graph done!")

# Find expansion areas
expansion_areas = data[
    (data["DemandLevel"] == "High") &
    (data["StorePresence"] == "No")
]

print("Expansion areas found!")

# Create map
print("Creating map...")

m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add markers
for i, row in data.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Region"]
    ).add_to(m)

# Highlight expansion areas
for i, row in expansion_areas.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=10,
        color="red",
        fill=True
    ).add_to(m)

# Save map
m.save("map.html")

print("Map created successfully!")