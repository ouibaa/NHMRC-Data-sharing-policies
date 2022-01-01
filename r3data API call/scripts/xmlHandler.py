import xmlschema
import pandas
import requests
from pprint import pprint
from xml.etree import ElementTree as ET
import pickle

# CONSTANTS
NS = {'re3': 'http://www.re3data.org/schema/2-2'}

def extractRepoList(xmlLoc, saveLoc):
    tree = ET.parse(xmlLoc)
    root = tree.getroot()
    idlist = []
    for repo in root.findall('repository'):
        id = repo.find('id').text
        idlist.append(id)
    with open(saveLoc, 'wb') as f:
        pickle.dump(idlist, f)
    f.close()
    return idlist

def extractRepoListByTag(idlist, xmlLoc, saveLoc, tag):
    idlistbytag = []
    for id in idlist:
        idloc = xmlLoc + "/" + id + ".xml"
        tree = ET.parse(idloc)
        root = tree.getroot()
        for repo in tree.findall('re3:repository', NS):
            subjects = repo.findall('re3:subject', NS)
            for subject in subjects:
                if subject.text == tag:
                    idlistbytag.append(id)
    saveLoc = saveLoc + '/' + tag + '.pkl'
    with open(saveLoc, 'wb') as f:
        pickle.dump(idlistbytag, f)
    return idlistbytag
    
def find(element, item):
    try:
        item = "re3:" + item
        res = element.find(item, NS)
        return res.text
    except:
        return(" ")


def extractRepoData(repolist, xmlLoc, saveLoc):
    for id in repolist:
        idloc = xmlLoc + "/" + id + ".xml"
        tree = ET.parse(idloc)
        root = tree.getroot()
        repo = tree.find('re3:repository', NS)
        repositoryIdentifier = id
        # Repo name
        repositoryName = find(repo, "repositoryName")
        # Repo URL
        repositoryName = find(repo, "repositoryURL")
        # Repo contact
        repositoryContacts = ""
        repositoryContact = repo.findall("re3:repositoryContact", NS)
        for contact in repositoryContact:
            repositoryContacts += contact.text + " "
        # Repo size
        repositorySize = find(repo, "size")
        # Repo language
        repositoryLanguage = find(repo, "repositoryLanguage")
        # Repo data/service provider status
        repositoryProviderType = find(repo, "providerType")

        for institution in repo.findall('re3:institution', NS):
            # Institution name
            institutionName = find(institution, "institutionName")
            # Country
            institutionCountry = find(institution, "institutionCountry")
            # Responsibility type
            responsibilityType = find(institution, "responsibilityType")
            # Institution type
            institutionType = find(institution, "institutionType")
            # Institution URL
            institutionURL = find(institution, "institutionURL")
        policies = ""
        for policy in repo.findall("re3:policy", NS):
            # Repo policy name
            policyName = find(policy, "policyName")
            # Repo policy URL
            policyURL = find(policy, "policyURL")
            # join and append to policies list
            pol = policyName + "(" + policyURL + ")"
            policies += pol + " "
        for databaseAccess in repo.findall("re3:databaseAccess", NS):
            # Database access type
            dbAccess = find(databaseAccess, "databaseAccessType")
        for databaseLicense in repo.findall("re3:databaseLicense", NS):
            # Database license name
            dbLicenseName = find(databaseLicense, "databaseLicenseName")
            # Database license URL
            dbLicenseURL = find(databaseLicense, "databaseLicenseURL")
        for dataAccess in tree.findall("re3:dataAccess", NS):
            # Data access type
            # Data access retriction
        # for dataLicense in tree.findall("re3:dataLicense", NS):
        #     # Data license name
        #     # data license url
        # for dataUpload in tree.findall("re3:dataUpload", NS):
        #     # data upload type
        #     # data upload restriction
        # for metadataStandard in tree.findall("re3:metadataStandard", NS):
        #     # metadata Standard Name
        #     # metadata Standard URL




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


