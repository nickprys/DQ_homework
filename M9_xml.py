import sys
import os
import xml.etree.ElementTree as ET
from datetime import date

# Path adjustment
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
import funct_dq

file_path = 'input.xml'
try:
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("Data successfully read from the file")

    # Uncomment the below lines if you want to delete the file after parsing
    # os.remove(file_path)
    # print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)  # Exit the script as there's no file to process

file_type_gen = root.get('file_type_gen')

for detail in root.findall('file_type_detail'):
    if file_type_gen == 'adv' and detail.find('adv_text') is not None:
        adv_data = detail.find('adv_text').text
        x = funct_dq.norm_text(adv_data)
        y = funct_dq.add_space_after_dot(x)
        print(y)

    elif file_type_gen == 'shop':
        fuel_type_element = detail.find('fuel_type')
        if fuel_type_element is not None:
            fuel_type = fuel_type_element.text
            if fuel_type == 'diesel':
                diesel_text = detail.find('diesel').text if detail.find('diesel') is not None else "No diesel info found"
                print(diesel_text)
            elif fuel_type == 'gas':
                gas_text = detail.find('gas').text if detail.find('gas') is not None else "No gas info found"
                print(gas_text)

    elif file_type_gen == 'news':
        new_text_element = detail.find('new_text')
        city_name_element = detail.find('city_name')
        if new_text_element is not None and city_name_element is not None:
            today = str(date.today())
            print(today + ' In the city ' + city_name_element.text + ' ' + new_text_element.text)