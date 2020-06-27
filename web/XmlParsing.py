import xml.etree.ElementTree


def getCountryName(element):
    for child in element.getChildren():
        if child.tag.__eq__("country"):
            print(child)


tree = xml.ElementTree.parse("country_data.xml")
root = tree.getroot()
print("root tag: ", root.tag)
getCountryName(root)
