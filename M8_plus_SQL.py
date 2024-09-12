import json
import sys
import os
from datetime import date

# Add the parent directory to the sys.path
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)

# Import your modules
import funct_dq
from M10v2 import DatabaseManager  # Adjust import statement as per actual module/file structure

file_path = 'input - news.json'
db = DatabaseManager('test2.db')  # Initialize the DatabaseManager with SQLite database file

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("Data successfully read from the file.")

    # Deleting the file could be problematic if errors occur during processing, consider this operation carefully
    #os.remove(file_path)
    #print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)  # exit script if file not found

adv_data = str(data['file_type_details'][0]['adv_text'])

if data['file_type_gen'] == 'adv':
    x = funct_dq.norm_text(adv_data)
    y = funct_dq.add_space_after_dot(x)
    print(y)
    db.insert_adv(y)  # Save to database

elif data['file_type_gen'] == 'shop':
    for detail in data['file_type_details']:
        if 'fuel_type' in detail:
            fuel_type = detail['fuel_type']
            info = detail.get(fuel_type, 'No info provided')
            print(info)
            db.insert_shop(fuel_type, info)  # Save to database

elif data['file_type_gen'] == 'news':
    for detail in data['file_type_details']:
        if 'city_name' in detail and 'new_text' in detail:
            today = str(date.today())
            city_name = detail['city_name']
            new_text = detail['new_text']
            full_message = f"{today} In the city {city_name} {new_text}"
            print(full_message)
            db.insert_news(today, city_name, new_text)  # Save to database

