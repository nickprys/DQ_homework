import sys
import json
import os
from datetime import date
from M10 import DatabaseManager  # Adjust this path if necessary

module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
import funct_dq

file_path = 'input - news.json'
db_path = 'test1.db'
db_manager = DatabaseManager(db_path)

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("Data successfully read from the file")

    # Uncomment these lines if you want to delete the file after processing
    # os.remove(file_path)
    # print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)  # Exit the script as there's no file to process

today = str(date.today())
for i, detail in enumerate(data['file_type_details']):
    file_type = detail['file_type']

    if file_type == 'adv':
        adv_text = funct_dq.norm_text(detail['adv_text'])
        content = funct_dq.add_space_after_dot(adv_text)
        title = f"Advertisement {i + 1}"
        print(content)

    elif file_type == 'shop':
        fuel_type = detail['fuel_type']
        if fuel_type in ['diesel', 'gas']:
            content = detail[fuel_type]
            title = f"Shop info {i + 1} - {fuel_type}"
            print(content)

    elif file_type == 'news':
        content = f"{today} In the city {detail['city_name']} {detail['new_text']}"
        title = f"News {i + 1}"
        print(content)

    if content:
        db_manager.insert_record(file_type, title, content)

db_manager.close()

db_manager.close()