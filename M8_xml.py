import xml.etree.ElementTree as ET

xml_file = ET.parse('testxml.xml')





root = xml_file.getroot()


for year in root.iter('year'):
    year.text = str(int(year.text) + 1)


xml_file.write('xml_new.xml')



