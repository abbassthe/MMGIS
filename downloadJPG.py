# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:15:36 2023

@author: User
"""
import requests
from bs4 import BeautifulSoup
import os

def collect(y, m, d):
    url = f'https://e4ftl01.cr.usgs.gov/ECOB/ECOSTRESS/ECO2LSTE.001/{y}.{m}.{d}/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    # Create a directory to store downloaded files
    download_dir = f"{y}_{m}_{d}_files"
    os.makedirs(download_dir, exist_ok=True)

    # Find all links on the web page
    links = soup.find_all('a')
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
    }
    for link in links:
        href = link.get('href')
        if href and href.endswith('.jpg') :  # Filter links to only download .tif files
            file_url = f"{url}{href}"
            file_name = os.path.join(download_dir, href)

            # Download the file
            
            response = requests.get(file_url, headers = headers)
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")

if __name__ == "__main__":
    year = "2023"
    month = "10"
    day = "06"
    collect(year, month, day)


