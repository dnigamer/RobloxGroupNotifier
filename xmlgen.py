import xml.etree.cElementTree as ET


def generate_xml(profile, message, date, directory):
    root = ET.Element("Response")
    processed = profile + " said " + message + " at " + date
    ET.SubElement(root, "Say", voice="Alice").text = processed
    tree = ET.ElementTree(root)
    tree.write(directory)
