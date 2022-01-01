import xmlschema
import pandas as pd
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
    repos = pd.DataFrame()
    for id in repolist:
        idloc = xmlLoc + "/" + id + ".xml"
        tree = ET.parse(idloc)
        root = tree.getroot()
        repo = tree.find('re3:repository', NS)
        repositoryIdentifier = id
        # Repo name
        repositoryName = find(repo, "repositoryName")
        # Repo URL
        repositoryURL = find(repo, "repositoryURL")
        # Repo contact
        repositoryContacts = ""
        for contact in repo.findall("re3:repositoryContact", NS):
            repositoryContacts += contact.text + " "
        # Repo size
        repositorySize = find(repo, "size")
        # Repo language
        repositoryLanguage = find(repo, "repositoryLanguage")
        # Repo data/service provider status
        repositoryProviderType = find(repo, "providerType")

        repoDict = {
            "ID": repositoryIdentifier,
            "Repository_Name": repositoryName,
            "Repository_URL": repositoryURL,
            "Repository_Contacts": repositoryContacts,
            "Repository_Size": repositorySize,
            "Repository_Language": repositoryLanguage,
            "Repository_Provider_Type": repositoryProviderType
        }

        for institution in repo.findall('re3:institution', NS):
            # Institution name
            institutionName = find(institution, "institutionName")
            repoDict["Institution_Name"] = institutionName
            # Country
            institutionCountry = find(institution, "institutionCountry")
            repoDict["Institution_Country"] = institutionCountry
            # Responsibility type
            responsibilityType = find(institution, "responsibilityType")
            repoDict["Institution_Responsibility_Type"] = responsibilityType
            # Institution type
            institutionType = find(institution, "institutionType")
            repoDict["Institution_Type"] = institutionType
            # Institution URL
            institutionURL = find(institution, "institutionURL")
            repoDict["Institution_URL"] = institutionURL
        policies = ""
        for policy in repo.findall("re3:policy", NS):
            # Repo policy name
            policyName = find(policy, "policyName")
            # Repo policy URL
            policyURL = find(policy, "policyURL")
            # join and append to policies list
            pol = policyName + "(" + policyURL + ")"
            policies += pol + " "
        repoDict["Policies"] = policies
        dbAccesses = ""
        for databaseAccess in repo.findall("re3:databaseAccess", NS):
            # Database access type
            dbAccess = find(databaseAccess, "databaseAccessType")
            dbAccesses += dbAccess + " "
        repoDict["Database_Accesses"] = dbAccesses
        dbLicenses = ""
        for databaseLicense in repo.findall("re3:databaseLicense", NS):
            # Database license name
            dbLicenseName = find(databaseLicense, "databaseLicenseName")
            # Database license URL
            dbLicenseURL = find(databaseLicense, "databaseLicenseURL")
            #join and append
            dbLic = dbLicenseName + " (" + dbLicenseURL + ")"
            dbLicenses += dbLic + " "
        repoDict["Database_Licenses"] = dbLicenses
        dataAccesses = ""
        for dataAccess in repo.findall("re3:dataAccess", NS):
            # Data access type
            dataAccessType = find(dataAccess, "dataAccessType")
            # Data access retriction
            restrictions = ""
            for dataAccessRestriction in dataAccess.findall("dataAccessRestriction", NS):
                text = ""
                try:
                    text = dataAccessRestriction.text
                except:
                    text = ""
                restrictions += dataAccessRestriction.text + "/"
            #Join
            dataAccessInfo = dataAccessType + " " + restrictions
            dataAccesses += dataAccessInfo + " "
        repoDict["Data_Accesses"] = dataAccesses
        dataLicenses = ""
        for dataLicense in repo.findall("re3:dataLicense", NS):
            # Data license name and URL
            dLN = find(dataLicense, "dataLicenseName")
            dLURL = find(dataLicense, "dataLicenseURL")
            # join and concat
            dL = dLN + " (" + dLURL + ")"
            dataLicenses += dL + " "
        repoDict["Data_Licenses"] = dataLicenses
        # for dataUpload in repo.findall("re3:dataUpload", NS):
        #     # data upload type
        #     # data upload restriction
        # for metadataStandard in repo.findall("re3:metadataStandard", NS):
        #     # metadata Standard Name
        #     # metadata Standard URL
        ### ALL COMPONENTS
        repos = repos.append(repoDict, ignore_index = True)
    print(repos)
    repos.to_csv(saveLoc, index=False)
    return repos

