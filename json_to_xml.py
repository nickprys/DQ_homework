import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

json_data = {
    "file_type_gen": "adv",
    "file_type_details": [
        {"file_type": "adv", "adv_text": "HelLo THis is the tEst text.HHH"},
        {"file_type": "shop", "fuel_type": "gas", "gas": "gas cost 10", "diesel": "diesel cost 7"},
        {"file_type": "news", "new_text": "Airplane crash", "city_name": "Chicago"}
    ]
}

root = ET.Element("data")
root.set('file_type_gen', json_data['file_type_gen'])

for item in json_data["file_type_details"]:
    detail = ET.SubElement(root, "file_type_detail")
    for key, value in item.items():
        sub_elem = ET.SubElement(detail, key)
        sub_elem.text = str(value)

# Use the prettify function to get a pretty-printed string
pretty_xml = prettify(root)

# Write the pretty-printed string to a file
with open('output.xml', 'w') as xml_file:
    xml_file.write(pretty_xml)