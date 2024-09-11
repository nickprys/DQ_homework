import sys
import os
from datetime import date

# Add the parent directory to the sys.path
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
import funct_dq

file_path = 'input.txt'
data = {}

try:
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ', 1)
            data[key] = value
    print("Data successfully read from the file")

    # Proceed to delete the file
    #os.remove(file_path)
    #print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)  # Exit if file is not found

file_type_gen = data['file_type_gen']

# Processing based on 'file_type_gen'
if file_type_gen == 'adv':
    adv_text = data['adv_text']
    formatted_text = funct_dq.add_space_after_dot(funct_dq.norm_text(adv_text))
    print(formatted_text)

elif file_type_gen == 'shop':
    fuel_type = data.get('fuel_type')
    if fuel_type == 'diesel':
        print(data.get('diesel', 'Diesel info not available'))
    elif fuel_type == 'gas':
        print(data.get('gas', 'Gas info not available'))

elif file_type_gen == 'news':
    city_name = data.get('city_name', 'Unknown city')
    new_text = data.get('new_text', 'No news text provided')
    today = str(date.today())
    print(f'{today} In the city {city_name} {new_text}')