# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:58:49 2023

@author: User
"""
import math
import os
import xml.etree.ElementTree as ET
import folium
from folium.plugins import HeatMap

# Function to convert latitude and longitude to X, Y, Z components
def lat_lon_to_xyz(latitude, longitude):
    radius = 6371  # Earth radius in km
    lat_rad = latitude * (3.141592653589793 / 180)
    lon_rad = longitude * (3.141592653589793 / 180)
    x = radius * math.cos(lat_rad) * math.cos(lon_rad)
    y = radius * math.cos(lat_rad) * math.sin(lon_rad)
    z = radius * math.sin(lat_rad)
    return x, y, z

# Directory containing the XML files
xml_directory = "C:\Users\User\Desktop\tempIvis\2023_10_06_files"

# Loop through each XML file in the directory
for filename in os.listdir(xml_directory):
    if filename.endswith(".xml"):
        xml_path = os.path.join(xml_directory, filename)

        # Parse the XML file to extract bounding coordinates
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Assuming XML structure has elements for latitude and longitude, modify the code accordingly
        latitude = float(root.find("latitude").text)
        longitude = float(root.find("longitude").text)

        # Convert latitude and longitude to X, Y, Z components
        x, y, z = lat_lon_to_xyz(latitude, longitude)

        # Create a directory for X data
        x_directory = os.path.splitext(xml_path)[0]  # Remove .xml extension
        os.makedirs(x_directory, exist_ok=True)

        # Save X data to a file
        x_file_path = os.path.join(x_directory, "x.txt")
        with open(x_file_path, "w") as x_file:
            x_file.write(f"X: {x}\nY: {y}\nZ: {z}")

        # Create a directory for JPG files
        jpg_directory = os.path.join(x_directory, "jpg_files")
        os.makedirs(jpg_directory, exist_ok=True)

        # Create a Folium map for heatmap
        m = folium.Map(location=[latitude, longitude], zoom_start=4)

        # Prepare the data for the heatmap (list of lists with [lat, lon, intensity])
        heat_data = [[latitude, longitude, 1]]  # Adjust intensity as needed

        # Add a heatmap layer to the map based on data intensity
        HeatMap(heat_data, radius=15).add_to(m)

        # Save the map as an HTML file
        map_html_path = os.path.join(jpg_directory, "spatial_heatmap.html")
        m.save(map_html_path)

        # You can generate JPG images from the HTML using a library like Selenium if needed


