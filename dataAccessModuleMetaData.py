from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
#2023
#10
#06
#ECO2LSTE.001
#spaceappsaubteam
#d84tUeA3u*58TKW
#enter data in the form yyyy,mm,dd
def get_meta_data(year,month,day,file_dir,folder,username,password):
   options = webdriver.ChromeOptions()
   options.add_argument('headless')
   options.add_experimental_option("prefs", {
    "download.default_directory": file_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
   })
   driver = webdriver.Chrome(chrome_options=options)
   #getting authantication
   driver.get(f'https://{username}:{password}@urs.earthdata.nasa.gov/oauth/authorize?scope=uid&app_type=401&client_id=ijpRZvb9qeKCK5ctsn75Tg&response_type=code&redirect_uri=https%3A%2F%2Fe4ftl01.cr.usgs.gov%2Foauth&state=aHR0cHM6Ly9lNGZ0bDAxLmNyLnVzZ3MuZ292Ly9FQ09CL0VDT1NUUkVTUy9FQ08yTFNURS4wMDEvMjAyMy4xMC4wNi9FQ09TVFJFU1NfTDJfTFNURV8yOTc2NF8wMDFfMjAyMzEwMDZUMDI1OTA1XzA2MDFfMDEuaDUueG1s')
   cookies = driver.get_cookies()
   s = requests.Session()
   for cookie in cookies:
      s.cookies.set(cookie['name'], cookie['value'])
   driver.get(f'https://e4ftl01.cr.usgs.gov//ECOB/ECOSTRESS/{folder}/{year}.{month}.{day}/')
   elements = driver.find_elements(By.TAG_NAME,'a')
   links=[]
   for i in range(0,len(elements)-1):
        text =  elements[i].get_attribute("outerHTML")
        links.append(text)
   for i in range(0,len(elements)-1):
      if links[i].__contains__(".xml"):
           end = links[i].find('x')
           print("got "+links[i][9:end+3])
           #driver.get('https://e4ftl01.cr.usgs.gov//ECOB/ECOSTRESS/ECO2LSTE.001/2023.10.06/'+f'{links[i][9:end+3]}')
           response  = s.get('https://e4ftl01.cr.usgs.gov//ECOB/ECOSTRESS/ECO2LSTE.001/2023.10.06/'+f'{links[i][9:end+3]}')
           with open(f'{links[i][9:end+3]}', 'wb') as file:
            file.write(response.content)
get_meta_data(2023,10,'Missions\data','Missions','ECO2LSTE.001','spaceappsaubteam','d84tUeA3u*58TKW')
