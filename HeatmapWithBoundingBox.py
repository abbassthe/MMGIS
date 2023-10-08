# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:01:38 2023

@author: Admin
"""

import os
import folium
from folium.plugins import HeatMap


# Specify the path to the root directory (replace with your actual path)
root_directory = r'C:\Users\Admin\OneDrive - American University of Beirut\Desktop\Fatima\NASA Space Apps Callenge\z'

# Initialize a list to store bounding boxes (latitudes and longitudes)
bounding_boxes = []

# Iterate over each item in the root directory
for xi_folder in os.listdir(root_directory):
    xi_path = os.path.join(root_directory, xi_folder)
    
    # Check if the item is a directory
    if os.path.isdir(xi_path):
        
        # Extract x coordinate from the folder name
        x_coordinate = float(xi_folder.split('_')[0])
        
        # Iterate over jpg files in xi folder
        for jpg_file in os.listdir(xi_path):
            if jpg_file.endswith('.jpg'):
                # Extract y coordinate from the filename
                y_coordinate = float(os.path.splitext(jpg_file)[0].split('_')[0])
                
                # Calculate bounding box for the tile with a radius of 70 meters
                bounding_boxes.append((x_coordinate + 0.000630, y_coordinate + 0.000630))  # Adjust based on your needs
                bounding_boxes.append((x_coordinate + 0.000630, y_coordinate - 0.000630))
                bounding_boxes.append((x_coordinate - 0.000630, y_coordinate - 0.000630))
                bounding_boxes.append((x_coordinate - 0.000630, y_coordinate + 0.000630))

# Create a Folium map centered at the mean of all coordinates
mean_latitude = sum(lat for lat, lon in bounding_boxes) / len(bounding_boxes)
mean_longitude = sum(lon for lat, lon in bounding_boxes) / len(bounding_boxes)
map_center = [mean_latitude, mean_longitude]

# Create a Folium map
heatmap_map = folium.Map(location=map_center, zoom_start=5)

# Add a HeatMap layer with bounding boxes
HeatMap(bounding_boxes).add_to(heatmap_map)

# Save the map as an HTML file
heatmap_map.save('heatmap_tiles.html')

