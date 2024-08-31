import sys
import os
import xml.etree.ElementTree as ET
from datetime import date

# Path adjustment
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
import funct_dq

file_path = 'output.xml'
try:
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("Data successfully read from the file")

    # proceed to delete the file
    os.remove(file_path)
    print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")

file_type_gen = root.get('file_type_gen')

for detail in root.findall('file_type_detail'):
    if file_type_gen == 'adv' and detail.find('adv_text') is not None:
        adv_data = detail.find('adv_text').text
        x = funct_dq.norm_text(adv_data)
        y = funct_dq.add_space_after_dot(x)
        print(y)

    elif file_type_gen == 'shop' and detail.find('fuel_type').text == 'diesel':
        print(detail.find('diesel').text)

    elif file_type_gen == 'shop' and detail.find('fuel_type').text == 'gas':
        print(detail.find('gas').text)

    elif file_type_gen == 'news' and detail.find('new_text') is not None:
        today = str(date.today())
        print(today + ' In the city ' + detail.find('city_name').text + ' ' + detail.find('new_text').text)