import json
import sys
import os
from datetime import date

# Add the parent directory to the sys.path
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
# Now you can import your module
import funct_dq

file_path = 'input.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("Data successfully read from the file")

    # Now that the data is read, you can proceed to delete the file
    os.remove(file_path)
    print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")


adv_data = str(data['file_type_details'][0]['adv_text'])

if data['file_type_gen'] == 'adv':

    x = funct_dq.norm_text(adv_data)
    y = funct_dq.add_space_after_dot(x)
    print(y)

elif data['file_type_gen'] == 'shop' and data['file_type_details'][1]['fuel_type'] == 'diesel':
            print(data['file_type_details'][1]['diesel'])
elif data['file_type_gen'] == 'shop' and data['file_type_details'][1]['fuel_type'] == 'gas':
            print(data['file_type_details'][1]['gas'])
elif data['file_type_gen'] == 'news':
            today = str(date.today())
            print(today + ' ' + 'In the city' + ' ' + data['file_type_details'][2]['city_name'] + ' ' + data['file_type_details'][2]['new_text'])



    # Closing file
file.close()