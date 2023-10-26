def contextDataFunc(my_namespaces, wantDiginNameSpaces):
    contextDict = {}
    diginContextDict = \
        {
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "cim": "http://ucaiug.org/ns/CIM#",
            "eu": "http://iec.ch/TC57/CIM100-European#",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "nc": "http://entsoe.eu/ns/nc#"
        }
    for nameSpace in my_namespaces:
        if nameSpace == "md":
            continue
        contextDict[nameSpace] = my_namespaces[nameSpace]
        if wantDiginNameSpaces == True and nameSpace in diginContextDict:
            contextDict[nameSpace] = diginContextDict[nameSpace]
    contextDict["dcterms"] = "http://purl.org/dc/terms/"
    contextDict["dcat"] = "http://www.w3.org/ns/dcat#"
    contextDict["prov"] = "http://www.w3.org/ns/prov#"
    contextDict["xsd"] = "http://www.w3.org/2001/XMLSchema#"
    return contextDict