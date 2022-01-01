# R3DATA API documentation notes
_Weber Liu 01/01/2022_

## Interface access for API
Link:
    https://www.re3data.org/api/<api identifier>

## Procedure
1. Access repository index list
    - GET https://www.re3data.org/api/v1/repositories
2. Access and store repo ID list
    - /list/repository/id
    - For example: r3d100000004
3. Access individual repo from repo ID list
    - GET https://www.re3data.org/api/v1/repository/r3d100000004
    - CHECK: /r3d:repository/r3d:subject (list)/
        - CONTAINS "205 Medicine"
    - IF:
        - CONTAINS "205 Medicine":
            - SAVE: 
                - repositoryName
                - repositoryURL
                - re3data.orgIdentifier
## Scripts
1. API handler
    - accesses API and stores the file as xml
        - Searches for r3d:re3data.orgIdentifier and uses this as the file name
    - Saves ALL contents of the query result
    - Accepted arguments:
        1. apiAddress:string
        2. id:string
        3. saveloc:string
    - Function
        - request REST API
        - Parses response to etree
        - Saves etree response to xml using [id] and [saveloc]
    - Returns
        - parsed etree:ElementTree
    - Error handling
        - query address doesn't exist
2. XML handler
    - accesses XML files (either from API or directly from tree)
    - extracts relevant content
    - Accepted arguments:
        1. onlineMode:bool
        2. idList:[string]
        3. saveloc:string
    - Function
        - If onlineMode is True, 