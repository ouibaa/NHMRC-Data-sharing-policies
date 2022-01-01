from scripts import apiHandler, xmlHandler

# apiHandler.retrieveRepoList(saveLoc = "./data/repolist.xml")
idlist = xmlHandler.extractRepoList(xmlLoc = "./data/repolist.xml", saveLoc = "./data/repolist.pkl")
# for id in idlist:
#     apiHandler.retrieveRepo(id = id, saveLoc = "./data/repos")
#     print("Retrieved repository " + id)
repolist = xmlHandler.extractRepoListByTag(idlist = idlist, xmlLoc = "./data/repos/xml", saveLoc="./data", tag="205 Medicine")

# with open("data/xmllistby205 Medicine.pkl", "rb") as f:
#     repolist = pickle.load(f) 

xmlHandler.extractRepoData(repolist, xmlLoc = "./data/repos/xml", saveLoc="./data/extracted.csv")

