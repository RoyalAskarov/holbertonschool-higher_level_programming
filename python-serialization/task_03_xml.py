import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    # Create a root element named <data>
    root = ET.Element("data")

    # Iterate through dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Write the XML tree to the provided filename using ET.ElementTree
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.
    """
    try:
        # Parse the XML file using ET.parse
        tree = ET.parse(filename)
        root = tree.getroot()

        # Navigate through elements to reconstruct the dictionary
        # Note: XML data is treated as strings by default
        return {child.tag: child.text for child in root}
    except (FileNotFoundError, ET.ParseError):
        return None