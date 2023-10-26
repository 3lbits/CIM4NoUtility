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
    wantDiginNameSpaces = parameter["wantDiginNameSpaces"]

    if xmlToJsonLd == True:
        xmlToJsonLDConverter(companyUuid, companyName, isVersionOfUrl, docType, docTopic, docTitle, wantDiginNameSpaces)

    if jsonldToXml == True:
        jsonToXmlConverter(docTitle)