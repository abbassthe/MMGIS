#import xmltodict
#import json
#xml_file=open("ECOSTRESS_L2_LSTE_29775_014_20231006T194712_0601_01.h5.xml","r")
#xml_string=xml_file.read()
#python_dict=xmltodict.parse(xml_string)
#json_string=json.dumps(python_dict)
#print("The JSON string is:")
#print(json_string)
#with open("sample.json", "w") as outfile:
#    outfile.write(json_string)
import csv
import json
import xml.etree.ElementTree as ET
def xml2geojson(file):
    tree = ET.parse(f"{file}")
    root = tree.getroot()
    req = root.find('GranuleURMetaData')
    # Extract bounding coordinates
    west = float(req[9][0][0][0].text)
    north = float(req[9][0][0][1].text)
    east = float(req[9][0][0][2].text)
    south = float(req[9][0][0][3].text)
    x = (west + east) / 2
    y = (north + south) / 2
    JSon ={
         "useKeyAsName": f"{req[1].text}",
            "geometry": {
            "type": "polygon",
            "coordinates": [x, y]
            },

    }
    return JSon

json_object = json.dumps(xml2geojson("ECOSTRESS_L2_LSTE_29775_020_20231006T195854_0601_01.h5.xml"), indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
