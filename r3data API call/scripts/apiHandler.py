import xmlschema
import pandas
import requests
from pprint import pprint
from xml.etree import ElementTree as ET

# CONSTANTS 
API_ADDRESS = "https://www.re3data.org/api/v1/repository"

def retrieveRepoList(saveLoc):
    # Function retrieves the totality of the repo list
   url = "https://www.re3data.org/api/v1/repositories"
   response = requests.get(url)
   tree = ET.fromstring(response.text)
   
   with open(saveLoc, "wb") as f:
       f.write(ET.tostring(tree))

   return tree

def retrieveRepo(id, saveLoc):
    # Function retrieves the repo list
    url = API_ADDRESS + "/" + id
    response = requests.get(url)
    tree = ET.fromstring(response.text)
    saveLocPkl = saveLoc + "/pickle/" + id + ".pkl"
    saveLocXml = saveLoc + "/xml/" + id + ".xml"
    with open(saveLocPkl, "wb") as f:
        f.write(tree)
    with open(saveLocXml, "wb") as g:
        g.write(ET.tostring(tree))
    return tree



# my_schema = xmlschema.XMLSchema('API Schema/re3dataV2-2.xsd')
# url = "https://www.re3data.org/api/v1/repository/r3d100000004"
# response = requests.get(url)
# # print(response.text)

# ns = {'re3': 'http://www.re3data.org/schema/2-2'}
# tree = ET.fromstring(response.text)

# with open("APICall.xml", "wb") as f:
#     f.write(ET.tostring(tree))

# for repo in tree.findall('re3:repository', ns):
#     identifier = repo.find('re3:re3data.orgIdentifier', ns)
#     print(identifier.text)

# xs = xmlschema.XMLSchema('tests/test_cases/examples/vehicles/vehicles.xsd')
# xt = ElementTree.parse('tests/test_cases/examples/vehicles/vehicles.xml')
# root = xt.getroot()
# pprint(xs.elements['cars'].decode(root[0]))
# {'{http://example.com/vehicles}car': [{'@make': 'Porsche', '@model': '911'},
#                                       {'@make': 'Porsche', '@model': '911'}]}
# pprint(xs.elements['cars'].decode(xt.getroot()[1], validation='skip'))
# None
# pprint(xs.elements['bikes'].decode(root[1], namespaces={'vh': 'http://example.com/vehicles'}))
# {'@xmlns:vh': 'http://example.com/vehicles',
#  'vh:bike': [{'@make': 'Harley-Davidson', '@model': 'WL'},
#              {'@make': 'Yamaha', '@model': 'XS650'}]}


