# Telemark-120
> [!NOTE]
> The DIGIN10 model has been renamed to Telemark-120 (05.06.2024)

## Background

Integrations, exchange of models and data between systems and businesses will become an important and essential process for the energy industry. Today this process is often a based on one to one integrations between systems/applications and ad-hoc solutions. 

In «ElBits Data Standardization» ElBits wants to engage with the DSOs and the vendors to develop and standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. The outcome will be increased reuse of an interface, higher data quality and lower implementation cost for all system applications and interfaces. This again will contribute to more efficient operations and grid development. 

ElBits/DIGIN has developed a test model, the Telemark-120 model for the regional and local distribution grid, that can be used together with the NORDIC44 transmission grid model for the nordic TSO grid. The Telemark-120 model contains the whole grid from the transmission connection to the local end user.

 CGMES v3.0 using CIM17 is the basis for the profiles. CDPSM v2.0 is used as basis for the profiles that are not included in the CGMES v3.0. The Telemark-120 model contains two boundary model profiles, one between each model authority set (MAS). 

## Definitions

- CIM = Common Information Model
- CGM = Common Grid Model
- CGMES = Common Grid Model Exchange Standard
- MAS = Model Authority Set
- HV = High Voltage (in this model: transmission grid)
- IGM = Individual Grid Model
- MV = Medium Voltage (in this model: regional and local distribution grid)
- LV = Low Voltage (in this model: low voltage local distribution grid)
- PATL = Permanent Admissible Transmission Loading
- TATL = Temporarily Admissible Transmission Loading

## Versions

DIGIN10-24-v1.0 - A 40 bus power flow case for MV and LV according to CGMES v2.4 (CIM16). Kept in v2.0 release to show the transition. 

DIGIN10-30-v2.0 - A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). A release to show the transformation from CGMES v2.4 to CGMES v3.0.

DIGIN10-30-v2.1 -  A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). Including measurement value time series, meter reading time series and necessary asset references.

DIGIN10-30-v2.2 - A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). Including measurement value time series, meter reading time series and necessary asset references. A release that now includes JSON-LD as an alternative to CIMXML.

## Specifications

 A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). Including two Model Authority Sets (MAS), bilateral boundaries and reference data. The solution is done on the merged (MV1+LV1). This version includes measurement values and meter readings to allow power flow calculations based on real time data. The inclusion of measurements will also allow better estimation of future scenarios (steady state values are also based on the real time series).

This version does not include any extensions of the [CGMES v3.0](Telemark-120\docs\StandardReferences.adoc). In [CDPSM v2.0](Telemark-120\docs\StandardReferences.adoc) we have added cim:UsagePoint so that we can model the customer installation. In this version the instance file supporting CDPSM is only added to support cim:UsagePoint and to show how cim:Asset and cim:AssetInfo is connected to the cim:PowerSystemResource. The plan is to show how CGMES + CDPSM can support the Autofos project in upcoming versions. Significant updates have been made to the Equipment Operation (OP) to address cim:Measurement.

## Content

### Branches

v1.0 can be found in the branch release/digin10-v1.0

v2.0 can be found in the branch release/digin10-v2.0

v2.2 can be found in the branch release/digin10-v2.2

### Folder structure

**Asset:**

***Asset/CIMJSON-LD*** and ***Asset/CIMXML***

Example files for using CDPSM v2.0 (IEC 61968-13:2021)
  
- Example of individual asset component
- Catalog data from manufacturers
- MeterReading
- ReadingQuality
- Customer profiles for both MV and LV

**Grid**

***Grid/CIMJSON-LD*** and ***Grid/CIMXML***

CGMES v3.0 serialised using CIMXML(IEC 61970-552)

The Telemark-120 model contains the following

- Profiles according to CGMES v3.0 using CIM17: DL, GL, SV, TP, SSH, EQ, OP
  - All instance files are according to CIMXML format (IEC 61970-552) which is based on RDF XML.
- Object regestry profiles for LV
- Reference data profiles
- Bilateral boundary models for interopability with NORDIC44 and between each MAS

**Schedule**
Split into year, month and day.

**Validation**

- Validation files from CIMdesk

**diagrams**

- Drawio images of EQ profile
- png/svg image files of full model from CIMdesk

**docs**

- Name Standards
- Modeling Guides
- Changelog for Converting to CGMES 3.0
- Known Issues for current version
- Release note

## Contribution

Please provide feedback in the case you are dicsovering any errors as Issues in the digin-energi/Grunnprofil repository. Suggested changes and updates needs to be merged to the "develop" branch and not "main". The order of information in files should follow the instructions in [Issue #217](https://github.com/digin-energi/Grunnprofil/issues/217).

## Resources
