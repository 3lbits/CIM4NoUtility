import defusedxml.ElementTree as ET
import json
import os
from functions import xmlPrefixListReplacer, valueDataTypeConverter
from contextData import contextDataFunc
from documentData import documentDataClass
from configPicker import configPicker

dir_path = os.path.dirname(os.path.realpath(__file__))

def xmlToJsonLDConverter(companyUuid, companyName, isVersionOfUrl, docType, docTopic, docTitle, wantDiginNameSpaces):

    inputFilePath = f"{dir_path}\_data\CIMXML\{docTitle}.xml"
    outputFilePath = f"{dir_path}\_data\JSON-LD\{docTitle}.jsonld"

    config = configPicker(docType, docTopic)

    my_namespaces = dict([node for _, node in ET.iterparse(inputFilePath, events=['start-ns'])])

    OutputJsonLD = {}

    # Context

    jsonldContext = contextDataFunc(my_namespaces, wantDiginNameSpaces)

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

    xmlMainTagList = xmlPrefixListReplacer(list(config.keys()), my_namespaces)
    configMainTagList = list(config.keys())

    for i in range(0, len(configMainTagList)):
        xmlMainTag = xmlMainTagList[i]
        configMainTag = configMainTagList[i]

        for mainTags in root.findall(xmlMainTag):
            xmlMainAttributeList = xmlPrefixListReplacer(list(config[configMainTag]['mainAttributes'].keys()), my_namespaces)
            configMainAttributeList = list(config[configMainTag]['mainAttributes'].keys())

            # MainAttributes ######################################
            dictionaryClass = {}

            for i in range(0, len(xmlMainAttributeList)):
                xmlMainAttribute = xmlMainAttributeList[i]
                configMainAttribute = configMainAttributeList[i]

                if mainTags.get(xmlMainAttribute)[:2] == '#_':
                    mainAttributeValue = f'urn:uuid:{mainTags.get(xmlMainAttribute)[2:]}'
                elif mainTags.get(xmlMainAttribute)[:2] != '#_' and mainTags.get(xmlMainAttribute)[:1] == '_':
                    mainAttributeValue = f"urn:uuid:{mainTags.get(xmlMainAttribute)[1:]}"

                mainAttributeType = config[configMainTag]['mainAttributes'][configMainAttribute]['type']

                dictionaryClass["@id"] = valueDataTypeConverter(mainAttributeValue, mainAttributeType)
                dictionaryClass["@type"] = configMainTag

            # Tags ################################################
            xmlTagList = xmlPrefixListReplacer(list(config[configMainTag]['tags'].keys()), my_namespaces)
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
            xmlAttributeTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'].keys()), my_namespaces)
            configAttributeTagList = list(config[configMainTag]['attributes'].keys())

            for i in range(0, len(xmlAttributeTagList)):
                xmlAttributeTag = xmlAttributeTagList[i]
                configAttributeTag = configAttributeTagList[i]

                attributeList = config[configMainTag]['attributes'][configAttributeTag]['list']

                if attributeList == True:
                        dictionaryClass[configAttributeTag] = []

                for attributeTags in mainTags.findall(xmlAttributeTag):
                    
                    xmlAttributeSubTagList = xmlPrefixListReplacer(list(config[configMainTag]['attributes'][configAttributeTag].keys()), my_namespaces)
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