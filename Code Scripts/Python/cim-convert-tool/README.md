# CIM Converter Tool

This is a tool made to convert CIMXML to CIMJsonLD and CIMJsonLD to CIMXML

## How to use it

### Step 0: Preinstallation guide

- This code is written with Python 3.10.5
- Libraries used:
  - defusedxml.ElementTree
  - json
  - os
  - xml.dom
  - decimal
  - datetime

### Step 1: Add data

In the folder _data you add either xml to CIMXML or JsonLD to JSON-LD

### Step 2: Choose config (Optional)

In the folder _config you can configure the output files by adding or removing complete classes or individual attributes

### Step 3: Set Parameters

In the parametes.py you need to sett companyUuid, companyName, isVersionOfUrl, if you want json and or xml. You must also configure documets which set the file parameters: docType, docTopic, docTitle, wantDiginNameSpaces.

The configured docTypes that are included:

```python
        case ("EQ", "Equipment"):
            config = configEqCim17
        case ("SSH", "Steady State Hypothesis"):
            config = configSshCim17
        case ("AS", "Asset"):
            config = configAsCim17
        case ("RD", "Base Voltage"):
            config = configBaseVoltageCim17
        case ("RD", "Geographical Region"):
            config = configGeographicalRegionCim17
        case ("BM", "Boundry"):
            config = configBmCim17
        case ("DL", "Diagram Layout"):
            config = configDlCim17
        case ("GL", "Geographical Location"):
            config = configGlCim17
        case ("OP", "Operation"):
            config = configOpCim17
        case ("SC", "Short Circuit"):
            config = configScCim17
        case ("AC", "Asset Catalogue"):
            config = configAcCim17
        case ("RD", "Measurement Value Source"):
            config = configMeasurementValueSourceCim17
        case ("RD", "Reading Quality Type"):
            config = configReadingQualityTypeCim17
        case ("RD", "Reading Type"):
            config = configReadingTypeCim17
        case ("CU", "Customer"):
            config = configCuCim17
        case ("SV", "State Variables"):
            config = configSvCim17
        case ("TP", "Topology"):
            config = configTpCim17
        case ("OR", "Object Reference"):
            config = configOrCim17
```

### Step 4: Run the script

You run the script from main.py. The xml output will end up in _data/CIMXML_Output. The jsonld output will end up in _data/JSON-LD
