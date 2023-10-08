# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:28:24 2023

@author: User
"""
import os
import xml.etree.ElementTree as ET

# Directory containing your XML files
# Directory containing your XML files
# Directory containing your XML files
xml_directory = 'C:\\Users\\User\\Desktop\\xml&jpg'



# Iterate through each XML file in the directory
for xml_file in os.listdir(xml_directory):
    if xml_file.endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_directory, xml_file))
        root = tree.getroot()

        # Extract bounding coordinates
        west = float(root.find('.//WestBoundingCoordinate').text)
        north = float(root.find('.//NorthBoundingCoordinate').text)
        east = float(root.find('.//EastBoundingCoordinate').text)
        south = float(root.find('.//SouthBoundingCoordinate').text)

        # Calculate x and y coordinates (you can choose any formula here)
        x = (west + east) / 2
        y = (north + south) / 2

        # Create the 'z' directory if it doesn't exist
        z_directory = os.path.join(xml_directory, 'z')
        if not os.path.exists(z_directory):
            os.mkdir(z_directory)

        # Create the 'x' directory if it doesn't exist
        x_directory = os.path.join(z_directory, str(int(x)))
        if not os.path.exists(x_directory):
            os.mkdir(x_directory)

        # Rename and move the JPG file
        jpg_file = os.path.splitext(xml_file)[0] + '.jpg'
        new_jpg_name = os.path.join(x_directory, str(int(y)) + '.jpg')
        os.rename(os.path.join(xml_directory, jpg_file), new_jpg_name)

