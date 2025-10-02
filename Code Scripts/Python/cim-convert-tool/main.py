from xmlToJsonLDConverter import xmlToJsonLDConverter
from jsonToXmlConverter import jsonToXmlConverter
from parameters import parameters

for parameter in parameters["documents"]:

    companyUuid = parameters["companyUuid"]
    companyName = parameters["companyName"]
    isVersionOfUrl = parameters["isVersionOfUrl"]
    xmlToJsonLd = parameters["xmlToJsonld"]
    jsonldToXml = parameters["jsonldToXml"]
    docType = parameter["docType"]
    docTopic = parameter["docTopic"]
    docTitle = parameter["docTitle"]
    wantCIM4NoUtilityNameSpaces = parameter["wantCIM4NoUtilityNameSpaces"]

    if xmlToJsonLd == True:
        xmlToJsonLDConverter(companyUuid, companyName, isVersionOfUrl, docType, docTopic, docTitle, wantCIM4NoUtilityNameSpaces)

    if jsonldToXml == True:
        jsonToXmlConverter(docTitle)