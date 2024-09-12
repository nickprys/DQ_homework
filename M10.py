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
            "CREATE TABLE IF NOT EXISTS adv (id INTEGER PRIMARY KEY, content TEXT, UNIQUE(content))",
            "CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY, content TEXT, UNIQUE(content))",
            "CREATE TABLE IF NOT EXISTS shop (id INTEGER PRIMARY KEY, content TEXT, UNIQUE(content))"
        ]
        for statement in table_statements:
            self.cursor.execute(statement)
        self.conn.commit()

    def insert_record(self, record_type, content):
        try:
            self.cursor.execute(f"INSERT INTO {record_type} (content) VALUES (?)", (content,))
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
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)  # Exit the script as there's no file to process

for detail in root.findall('file_type_detail'):
    content = None
    file_type = detail.find('file_type').text

    if file_type == 'adv' and detail.find('adv_text') is not None:
        adv_text = detail.find('adv_text').text
        normalized_text = funct_dq.norm_text(adv_text)
        formatted_text = funct_dq.add_space_after_dot(normalized_text)
        print(formatted_text)
        content = formatted_text

    elif file_type == 'shop':
        fuel_type_element = detail.find('fuel_type')
        if fuel_type_element is not None:
            fuel_type = fuel_type_element.text
            fuel_content = detail.find(fuel_type).text if detail.find(fuel_type) is not None else "Info not available"
            print(fuel_content)
            content = fuel_content

    elif file_type == 'news':
        new_text_element = detail.find('new_text')
        city_name_element = detail.find('city_name')
        if new_text_element is not None and city_name_element is not None:
            today = str(date.today())
            news_content = today + ' In the city ' + city_name_element.text + ' ' + new_text_element.text
            print(news_content)
            content = news_content

    if content:
        db_manager.insert_record(file_type, content)

db_manager.close()