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
                