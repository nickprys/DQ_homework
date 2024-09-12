import sys
import os
import sqlite3
import xml.etree.ElementTree as ET
from datetime import date

# Path adjustment to include custom module
module_path = 'C:\\Users\\Mykola_Prysiazhniuk\\PycharmProjects\\DQ0802_functions_task4\\test_pac44'
sys.path.append(module_path)
import funct_dq

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS news (date TEXT, city TEXT, news TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS shop (fuel_type TEXT, info TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS adv (text TEXT)")
        self.conn.commit()

    def insert_news(self, date, city, news):
        exists = self.cursor.execute("SELECT * FROM news WHERE date=? AND city=? AND news=?", (date, city, news)).fetchone()
        if not exists:
            self.cursor.execute("INSERT INTO news (date, city, news) VALUES (?, ?, ?)", (date, city, news))
            self.conn.commit()

    def insert_shop(self, fuel_type, info):
        exists = self.cursor.execute("SELECT * FROM shop WHERE fuel_type=? AND info=?", (fuel_type, info)).fetchone()
        if not exists:
            self.cursor.execute("INSERT INTO shop (fuel_type, info) VALUES (?, ?)", (fuel_type, info))
            self.conn.commit()

    def insert_adv(self, text):
        exists = self.cursor.execute("SELECT * FROM adv WHERE text=?", (text,)).fetchone()
        if not exists:
            self.cursor.execute("INSERT INTO adv (text) VALUES (?)", (text,))
            self.conn.commit()

    def __del__(self):
        self.conn.close()

# Initialize the database manager
db_manager = DatabaseManager("test2.db")

file_path = 'input.xml'
try:
    tree = ET.parse(file_path)
    root = tree.getroot()
except FileNotFoundError:
    print("The file was not found.")
    sys.exit(1)

file_type_gen = root.get('file_type_gen')

for detail in root.findall('file_type_detail'):
    if file_type_gen == 'adv' and detail.find('adv_text') is not None:
        adv_data = detail.find('adv_text').text
        x = funct_dq.norm_text(adv_data)
        y = funct_dq.add_space_after_dot(x)
        db_manager.insert_adv(y)

    elif file_type_gen == 'shop':
        fuel_type_element = detail.find('fuel_type')
        if fuel_type_element is not None:
            fuel_type = fuel_type_element.text
            info_text = detail.find(fuel_type).text if detail.find(fuel_type) is not None else "No info found"
            db_manager.insert_shop(fuel_type, info_text)

    elif file_type_gen == 'news':
        new_text_element = detail.find('new_text')
        city_name_element = detail.find('city_name')
        if new_text_element is not None and city_name_element is not None:
            today = str(date.today())
            db_manager.insert_news(today, city_name_element.text, new_text_element.text)