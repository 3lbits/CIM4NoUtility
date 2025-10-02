import defusedxml.ElementTree as ET
import json
from functions import xmlPrefixListReplacer, valueDataTypeConverter
from _config.configEqCim17 import configEqCim17
from _config.configSshCim17 import configSshCim17
from _config.configAsCim17 import configAsCim17
from _config.configBaseVoltageCim17 import configBaseVoltageCim17
from _config.configGeographicalRegionCim17 import configGeographicalRegionCim17
from _config.configBmCim17 import configBmCim17
from _config.configDlCim17 import configDlCim17
from _config.configGlCim17 import configGlCim17
from _config.configOpCim17 import configOpCim17
from _config.configScCim17 import configScCim17
from _config.configAcCim17 import configAcCim17
from _config.configMeasurementValueSourceCim17 import configMeasurementValueSourceCim17
from _config.configReadingQualityTypeCim17 import configReadingQualityTypeCim17
from _config.configReadingTypeCim17 import configReadingTypeCim17
from _config.configCuCim17 import configCuCim17
from _config.configSvCim17 import configSvCim17
from _config.configTpCim17 import configTpCim17
from _config.configOrCim17 import configOrCim17
from contextData import contextDataClass
from documentData import documentDataClass
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def xmlToJsonLDConverter(companyUuid, companyName, isVersionOfUrl, docType, docTopic, docTitle):

    inputFilePath = f"{dir_path}\_data\CIMXML\{docTitle}.xml"
    outputFilePath = f"{dir_path}\_data\JSON-LD\{docTitle}.jsonld"

    if docType == "EQ":
        config = configEqCim17
    elif docType == "SSH":
        config = configSshCim17
    elif docType == "AS":
        config = configAsCim17
    elif docType == "RD" and docTopic == 'Base Voltage':
        config = configBaseVoltageCim17
    elif docType == "RD" and docTopic == 'Geographical Region':
        config = configGeographicalRegionCim17
    elif docType == "BM":
        config = configBmCim17
    elif docType == "DL":
        config = configDlCim17
    elif docType == "GL":
        config = configGlCim17
    elif docType == "OP":
        config = configOpCim17
    elif docType == "SC":
        config = configScCim17
    elif docType == "AC":
        config = configAcCim17
    elif docType == "RD" and docTopic == 'Measurement Value Source':
        config = configMeasurementValueSourceCim17
    elif docType == "RD" and docTopic == 'Reading Quality Type':
        config = configReadingQualityTypeCim17
    elif docType == "RD" and docTopic == 'Reading Type':
        config = configReadingTypeCim17
    elif docType == "CU":
        config = configCuCim17
    elif docType == "SV":
        config = configSvCim17
    elif docType == "TP":
        config = configTpCim17
    elif docType == "OR":
        config = configOrCim17

    rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    cim = "http://ucaiug.org/ns/CIM#"
    md = "http://iec.ch/TC57/61970-552/ModelDescription/1#"
    eu = "http://iec.ch/TC57/CIM100-European#"
    skos = "http://www.w3.org/2004/02/skos/core#"
    nc = "http://entsoe.eu/ns/nc#"

    OutputJsonLD = {}

    # Context

    if docTopic == "Reading Quality Type":
        isSkos = True
    elif docTopic == "Reading Type":
        isSkos = True
    else:
        isSkos = False

    if docType == "OR":
        isNc = True
    else:
        isNc = False

    jsonldContext = contextDataClass(isSkos, isNc) \
        .contextDataFunc()

    OutputJsonLD["@context"] = jsonldContext
    graphList = []

    # FullModel
    documentDataClass(
        inputFilePath,
        docTitle,
        companyUuid,
        companyName,
        isVersionOfUrl,
        docType,
        OutputJsonLD
        ).documentDataFunc()

    # xmlInput
    tree = ET.parse(inputFilePath)
    root = tree.getroot()

    xmlMainTagList = xmlPrefixListReplacer(list(config.keys()), cim, eu, rdf, md, skos, nc)
    configMainTagList = list(config.keys())

    for i in range(0, len(configMainTagList)):
        xmlMainTag = xmlMainTagList[i]
        configMainTag = configMainTagList[i]

        for mainTags in root.findall(xmlMainTag):
            xmlMainAttributeList = xmlPrefixListReplacer(list(config[configMainTag]['mainAttributes'].keys()), cim, eu, rdf, md, skos, nc)
            configMainAttributeList = list(config[configMainTag]['mainAttributes'].keys())

            # MainAttributes ######################################
            dictionaryClass = {}

            for i in range(0, len(xmlMainAttributeList)):
                xmlMainAttribute = xmlMainAttributeList[i]
                configMainAttribute = configMainAttributeList[i]

                mainAttributeValue = f'urn:uuid:{mainTags.get(xmlMainAttribute)[1:]}'
                mainAttributeType = config[configMainTag]['mainAttributes'][configMainAttribute]['type']

                dictionaryClass["@id"] = valueDataTypeConverter(mainAttributeValue, mainAttributeType)
                dictionaryClass["@type"] = configMainTag

            # Tags ################################################
            xmlTagList = xmlPrefixListReplacer(list(config[configMainTag]['tags'].keys()), cim, eu, rdf, md, skos, nc)
            configTagList = list(config[configMainTag]['tags'].keys())

            for i in range(0, len(xmlTagList)):
                xmlTag = xmlTagList[i]
                configTag = configTagList[i]

                textType = config[configMainTag]['tags'][configTag]['type']
                textList = config[configMainTag]['tags'][configTag]['list']

                if textList == True: # Checking if Tag can be list
                    dictionaryClass[configTag] = []

                for tags in mainTags.findall(xmlTag):
                    
                    textValue = tags.text

                    # if configTag == 'cim:IdentifiedObject.mRID':
                    #     textValue = f'urn:uuid:{textValue}'
                    # elif configTag == 'nc:Name.mRID':
                    #     textValue = f'urn:uuid:{textValue}'
                    # elif configTag == 'nc:NameType.mRID':
                    #     textValue = f'urn:uuid:{textValue}'
                    # elif configTag == 'nc:NameTypeAuthority.mRID':
                    #     textValue = f'urn:uuid:{textValue}'

                    if textList == True: # Checking if Tag can be list
                        if 'CIMDatatype' in config[configMainTag]['tags'][configTag].keys(): # Checking if Tag has CIMDatatype
                            dictionaryClass[configTag].append({config[configMainTag]['tags'][configTag]['CIMDatatype']: valueDataTypeConverter(textValue, textType)})
                        else:
                            dictionaryClass[configTag].append(valueDataTypeConverter(textValue, textType))
                    else:
                        if 'CIMDatatype' in config[configMainTag]['tags'][configTag].keys(): # Checking if Tag has CIMDatatype
                            dictionaryClass[configTag] = {config[configMainTag]['tags'][configTag]['CIMDatatype']: valueDataTypeConverter(textValue, textType)}
                        else:
                            dictionaryClass[configTag] = valueDataTypeConverter(textValue, textType)
            
            # Attributes ##########################################
            xmlAttributeTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'].keys()), cim, eu, rdf, md, skos, nc)
            configAttributeTagList = list(config[configMainTag]['attributes'].keys())

            for i in range(0, len(xmlAttributeTagList)):
                xmlAttributeTag = xmlAttributeTagList[i]
                configAttributeTag = configAttributeTagList[i]

                attributeList = config[configMainTag]['attributes'][configAttributeTag]['list']

                if attributeList == True:
                        dictionaryClass[configAttributeTag] = []

                for attributeTags in mainTags.findall(xmlAttributeTag):
                    
                    xmlAttributeSubTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'][configAttributeTag].keys()), cim, eu, rdf, md, skos, nc)
                    configAttributeSubTagList = list(config[configMainTag]['attributes'][configAttributeTag].keys())

                    for i in range(0, len(xmlAttributeSubTagList)):
                        xmlAttributeSubTag = xmlAttributeSubTagList[i]
                        configAttributeSubTag = configAttributeSubTagList[i]
                        
                        if attributeTags.get(xmlAttributeSubTag) != None:
                            if attributeTags.get(xmlAttributeSubTag)[:2] == '#_':
                                attributeValue = f'urn:uuid:{attributeTags.get(xmlAttributeSubTag)[2:]}'
                            else:
                                attributeValue = attributeTags.get(xmlAttributeSubTag)\
                                    .replace("http://ucaiug.org/ns/CIM#", "cim:")\
                                    .replace("http://iec.ch/TC57/CIM100-European#", "eu:") # Handling conversion from "url" to prefix

                        attributeType = config[configMainTag]['attributes'][configAttributeTag][configAttributeSubTag]['type']

                        subDictionaryClass = {}
                        subDictionaryClass['@id'] = valueDataTypeConverter(attributeValue, attributeType)

                        if attributeList == True:
                            dictionaryClass[configAttributeTag].append(subDictionaryClass)
                        else:
                            dictionaryClass[configAttributeTag] = subDictionaryClass

            graphList.append(dictionaryClass)

    OutputJsonLD["@graph"] = graphList

    # Output

    # Converting output to json
    json_data = json.dumps(OutputJsonLD, indent=4, ensure_ascii=False)

    # Printing result
    # print(json_data)

    # Writing to file
    with open(outputFilePath, "w", encoding='utf8') as outfile:
        outfile.write(json_data)