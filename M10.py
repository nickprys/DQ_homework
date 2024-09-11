import sys
import os
import xml.etree.ElementTree as ET
from datetime import date
import sqlite3


# Database Manager Code
class DatabaseManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        table_statements = [
            "CREATE TABLE IF NOT EXISTS adv (id INTEGER PRIMARY KEY, title TEXT, content TEXT, UNIQUE(title))",
            "CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, title TEXT, content TEXT, UNIQUE(title))",
            "CREATE TABLE IF NOT EXISTS shop (id INTEGER PRIMARY KEY, title TEXT, content TEXT, UNIQUE(title))"
        ]
        for statement in table_statements:
            self.cursor.execute(statement)
        self.conn.commit()

    def insert_record(self, record_type, title, content):
        try:
            self.cursor.execute(f"INSERT INTO {record_type} (title, content) VALUES (?, ?)", (title, content))
            self.conn.commit()
            print(f"Record inserted into {record_type} table")
        except sqlite3.IntegrityError:
            print("Record already exists. Not inserting duplicate.")

    def close(self):
        self.conn.close()


# Path and module imports (update as necessary)
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
import funct_dq

file_path = 'output.xml'
db_manager = DatabaseManager('test1.db')  # Initialize database

try:
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("Data successfully read from the file")

    # proceed to delete the file
    # os.remove(file_path)
    # print("File has been deleted.")
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)  # Exit the script as there's no file to process

file_type_gen = root.get('file_type_gen')

for detail in root.findall('file_type_detail'):
    content = None
    # Extract the type of detail directly from the current element in the XML file
    file_type = detail.find('file_type').text

    # Handle 'adv' (advertisement) data type
    if file_type == 'adv' and detail.find('adv_text') is not None:
        # Normalize and format the advertisement text
        adv_text = detail.find('adv_text').text
        x = funct_dq.norm_text(adv_text)
        y = funct_dq.add_space_after_dot(x)
        print(y)  # Output the formatted advertisement text
        content = y  # Set content to the formatted text for database insertion

    # Handle 'shop' data type
    elif file_type == 'shop':
        # Safely obtain the fuel_type element, checking if it exists
        fuel_type_element = detail.find('fuel_type')
        if fuel_type_element is not None:
            fuel_type = fuel_type_element.text
            # Process based on specific fuel type
            if fuel_type == 'diesel':
                diesel_text = detail.find('diesel').text
                print(diesel_text)  # Output the diesel price information
                content = diesel_text  # Prepare content for database storage
            elif fuel_type == 'gas':
                gas_text = detail.find('gas').text
                print(gas_text)  # Output the gas price information
                content = gas_text  # Prepare content for database storage

    # Handle 'news' data type
    elif file_type == 'news' and detail.find('new_text') is not None:
        # Get today's date to prepend to the news content
        today = str(date.today())
        news_text = today + ' In the city ' + detail.find('city_name').text + ' ' + detail.find('new_text').text
        print(news_text)  # Output formatted news information
        content = news_text  # Set content for database insertion based on the news info

    # Insert content into the database if it has been set
    if content:
        db_manager.insert_record(file_type, detail.get('title', 'No Title'), content)
        # `detail.get('title', 'No Title')` safely fetches the 'title' attribute or defaults to 'No Title'