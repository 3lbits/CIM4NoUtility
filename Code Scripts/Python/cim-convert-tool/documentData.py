import defusedxml.ElementTree as ET
from datetime import datetime, timedelta

def modellInfoFunc(
    fullModelRdfAbout,
    fullModelModelCreated,
    fullModelModelScenarioTime,
    docTitle,
    fullModelModelDescription,
    # fullModelModelVersion,
    companyUuid,
    companyName,
    isVersionOfUrl,
    docType,
    fullModelModelingAuthoritySet,
    fullModelProfileList,
    fullModelDependentOn,
    dictionary
    ):
    dateTimeNow = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    yearNow = datetime.utcnow().strftime("%Y")
    if fullModelModelScenarioTime != "": scenarioTime = datetime.strptime(fullModelModelScenarioTime, "%Y-%m-%dT%H:%M:%SZ") + timedelta(days=1)

    dictionary["@id"] = fullModelRdfAbout
    dictionary["@type"] = "dcat:Dataset"
    dictionary["prov:generatedAtTime"] = {
            "@value": dateTimeNow,
            "@type": "xsd:dateTime"
        }
    dictionary["dcterms:issued"] = {
            "@value": fullModelModelCreated,
            "@type": "xsd:date"
        }
    dictionary["dcterms:title"] = docTitle #DIGIN10-30-MV1_EQ
    dictionary["dcterms:description"] = [
        {
            "@value": fullModelModelDescription,
            "@language": "en"
        }
    ]
    # dictionary["dcat:version"] = fullModelModelVersion
    dictionary["dcterms:publisher"] = {
            "@id": f"urn:uuid:{companyUuid}", #Digin uuid
            "dcterms:title": companyName #Digin
        }
    if docType in ["SSH", "TP", "SV"] and fullModelModelScenarioTime != "":
        dictionary["dcterms:temporal"] = {
            "@type": "dcterms:PeriodOfTime",
            "dcat:startDate": { # --> Alle
                "@value": fullModelModelScenarioTime, # ScenarioTime
                "@type": "xsd:dateTime"
                },
                "dcat:endDate": { #  --> SSH, TP, SV
                    "@value": str(scenarioTime.strftime("%Y-%m-%dT%H:%M:%SZ")), # ScenarioTime + 1d
                    "@type": "xsd:dateTime"
                    }
            }
        dictionary["dcat:temporalResolution"] = { # --> SSH, TP, SV
                "@type": "xsd:duration",
                "@value": "PT1H"
            }
    elif fullModelModelScenarioTime != "":
        dictionary["dcterms:temporal"] = {
            "@type": "dcterms:PeriodOfTime",
            "dcat:startDate": { # --> Alle
                "@value": fullModelModelScenarioTime, # ScenarioTime
                "@type": "xsd:dateTime"
                }
            }

    dictionary["dcterms:rights"] = f"© {yearNow} Copyright"
    dictionary["dcterms:rightsHolder"] = companyName
    dictionary["dcterms:license"] = {
            "@id": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
            "dcterms:title": "CC BY-NC-SA 4.0"
    }
    dictionary["dcterms:accessRights"] = {
            "@id": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
            "dcterms:title": "PUBLIC"
        }
    dictionary["dcat:isVersionOf"] = {"@id": f"{isVersionOfUrl}{docTitle}"} #https://digin.no/baseprofile/DIGIN10-30-MV1_EQ
    dictionary["dcat:keyword"] = docType #EQ
    dictionary["dcterms:spatial"] = {"@id": fullModelModelingAuthoritySet}
    if fullModelProfileList != []: dictionary["dcterms:conformsTo"] = fullModelProfileList
    if fullModelDependentOn != "":
        dictionary["dcterms:references"] = [
            {
                "@id": fullModelDependentOn#,
                #"dcterms:title": docTitle #DIGIN10-30-MV1_EQ
            }
        ]
    return dictionary

class documentDataClass:
    def __init__(self,
                 inputFilePath, docTitle, companyUuid, companyName, isVersionOfUrl, docType, dictionary):

        fullModelRdfAbout = ""
        fullModelModelCreated = ""
        fullModelModelScenarioTime = ""
        fullModelModelDescription = ""
        # fullModelModelVersion = ""
        fullModelModelingAuthoritySet = ""
        fullModelProfileList = []
        fullModelDependentOn = ""

        tree = ET.parse(inputFilePath)
        root = tree.getroot()

        childList = []
        for childs in root:
                childList.append(childs.tag)
                if childs.tag == '{http://iec.ch/TC57/61970-552/ModelDescription/1#}FullModel': break
        fullModelIndex = childList.index('{http://iec.ch/TC57/61970-552/ModelDescription/1#}FullModel')

        fullModelRdfAbout = root[0].get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
        for i in range(0, len(root[fullModelIndex])):
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.created": fullModelModelCreated = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.scenarioTime": fullModelModelScenarioTime = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.description": fullModelModelDescription = root[fullModelIndex][i].text
                # if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.version": fullModelModelVersion = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.modelingAuthoritySet": fullModelModelingAuthoritySet = root[fullModelIndex][i].text
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.profile": fullModelProfileList.append({"@id": root[fullModelIndex][i].text})
                if root[fullModelIndex][i].tag == "{http://iec.ch/TC57/61970-552/ModelDescription/1#}Model.DependentOn": fullModelDependentOn = root[fullModelIndex][i].get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')

        self.fullModelJsonLd = modellInfoFunc(
                fullModelRdfAbout,
                fullModelModelCreated,
                fullModelModelScenarioTime,
                docTitle,
                fullModelModelDescription,
                # fullModelModelVersion,
                companyUuid,
                companyName,
                isVersionOfUrl,
                docType,
                fullModelModelingAuthoritySet,
                fullModelProfileList,
                fullModelDependentOn,
                dictionary
                )

    def documentDataFunc(self):
        return self.fullModelJsonLd