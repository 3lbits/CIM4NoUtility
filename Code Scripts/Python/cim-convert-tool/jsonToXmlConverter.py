import os
import json
from xml.dom import minidom

dir_path = os.path.dirname(os.path.realpath(__file__))

def createContext(rdf, dict):
    contextData = dict
    contextData["md"] = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
    for context in contextData:
        if context in ["dcterms", "dcat", "prov", "xsd"]:
            continue
        rdf.setAttribute(f"xmlns:{context}", contextData[context])

def createTextTag(root, tag, parentTag, text):
    var = root.createElement(tag)
    var.appendChild(root.createTextNode(text))
    parentTag.appendChild(var)

def createAttributeTag(root, tag, parentTag, attributeName, value):
    var = root.createElement(tag)
    var.setAttribute(attributeName, value)
    parentTag.appendChild(var)

def checkKey(dict, key):
    return dict.get(key) != None

def createFullModel(root, rdf, data):
    FullModel = root.createElement("md:FullModel")
    FullModel.setAttribute("rdf:about", data["@id"])
    rdf.appendChild(FullModel)
    createTextTag(root, "md:Model.created", FullModel, data["dcterms:issued"]["@value"])
    createTextTag(root, "md:Model.scenarioTime", FullModel, data["dcterms:description"][0]["@value"])
    createTextTag(root, "md:Model.description", FullModel, data["dcterms:temporal"]["dcat:startDate"]["@value"]) if checkKey(data, "dcterms:temporal") == True else None
    createTextTag(root, "md:Model.modelingAuthoritySet", FullModel, data["dcterms:spatial"]["@id"])
    if  checkKey(data, "dcterms:conformsTo") == True:
        for i in range(0, len(data["dcterms:conformsTo"])):
            createTextTag(root, "md:Model.profile", FullModel, data["dcterms:conformsTo"][i]["@id"])
    createTextTag(root, "md:Model.version", FullModel, "1")
    if  checkKey(data, "dcterms:references") == True:
        for i in range(0, len(data["dcterms:references"])):
            createAttributeTag(root, "md:Model.DependentOn", FullModel, "rdf:resource", data["dcterms:references"][i]["@id"])

def replacePrefixWithUrl(contextDict, data):
    prefixList = list(contextDict.keys())
    prefix = data.split(':')[0]
    if prefix in prefixList:
        return data.replace(f"{prefix}:", contextDict[prefix])
    else:
        return data

def createEntities(root, rdf, data):
    for i in range(0, len(data["@graph"])):
        
        childData = data["@graph"][i]
        childKeys = list(childData.keys())
        childTag = root.createElement(childData["@type"])
        rdf.appendChild(childTag)

        for i in range(0, len(childKeys)):
            childKey = childKeys[i]
            if childKey == "@type":
                continue
            if childKey == "@id":
                if data["dcat:keyword"] in {"SSH", "SC", "TP"}:
                    childTag.setAttribute("rdf:about", childData[childKey].replace("urn:uuid:", "#_"))
                else :
                    childTag.setAttribute("rdf:ID", childData[childKey].replace("urn:uuid:", "_"))
            else:
                if isinstance(childData[childKey], str):
                    createTextTag(root, childKey, childTag, childData[childKey])
                if isinstance(childData[childKey], float):
                    createTextTag(root, childKey, childTag, str(childData[childKey]))
                if isinstance(childData[childKey], int): #int and bool
                    createTextTag(root, childKey, childTag, str(childData[childKey]).lower())
                if isinstance(childData[childKey], dict):
                    attributeData = replacePrefixWithUrl(data["@context"], childData[childKey]["@id"])
                    createAttributeTag(root, childKey, childTag, "rdf:resource", attributeData.replace("urn:uuid:", "#_"))

def jsonToXmlConverter(docTitle):
    docTitle = docTitle
    path = f"{dir_path}\_data\JSON-LD\{docTitle}.jsonld"
    outputPath = f"{dir_path}\_data\CIMXML_Output\{docTitle}.xml"

    with open(path, 'r') as jsonFile:
        data = json.load(jsonFile)

    root = minidom.Document()
    rdf = root.createElement("rdf:RDF")
    root.appendChild(rdf)

    createContext(rdf, data["@context"])
    createFullModel(root, rdf, data)
    createEntities(root, rdf, data)

    xml_str = root.toprettyxml(encoding="UTF-8")

    with open(outputPath, 'wb') as xmlFile:
        xmlFile.write(xml_str)