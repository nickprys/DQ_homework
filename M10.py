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
        adv_text = detail.find('adv_text').text
        normalized_text = funct_dq.norm_text(adv_text)
        formatted_text = funct_dq.add_space_after_dot(normalized_text)
        print(formatted_text)
        content = formatted_text
        title = "Adv on " + date.today().strftime("%Y-%m-%d")

    # Handle 'shop' data type
    elif file_type == 'shop':
        fuel_type_element = detail.find('fuel_type')
        if fuel_type_element is not None:
            fuel_type = fuel_type_element.text
            fuel_content = detail.find(fuel_type).text if detail.find(fuel_type) is not None else "Info not available"
            print(fuel_content)
            content = fuel_content
            title = f"Shop update - {fuel_type} on " + date.today().strftime("%Y-%m-%d")

    # Handle 'news' data type
    elif file_type == 'news':
        new_text_element = detail.find('new_text')
        city_name_element = detail.find('city_name')
        if new_text_element is not None and city_name_element is not None:
            today = str(date.today())
            news_content = today + ' In the city ' + city_name_element.text + ' ' + new_text_element.text
            print(news_content)
            content = news_content
            title = f"News from {city_name_element.text} on " + date.today().strftime("%Y-%m-%d")

    # Insert content into the database if content and title have been set
    if content and title:
        db_manager.insert_record(file_type, title, content)