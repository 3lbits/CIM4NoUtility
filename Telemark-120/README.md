<<<<<<< HEAD
<<<<<<<< HEAD:Telemark-120/README.md
# Telemark-120
> [!NOTE]
> The DIGIN10 model has been renamed to Telemark-120 (05.06.2024)
========
# Welcome to the ElBits Utillity Standardization Community Platform
The goal of ElBits Data Standardization is to establish a best practice for the use of data exchange formats within the Norwegian (and international) electrical utility industry. To acheive this the whole electric utility industry must contribute. 
The Community platform shall serve as an arena for development of best practices and competence enhancement within the Norwegian electric utility industry.
>>>>>>>> develop:README.md

## :seedling: Get involved
All communication within the Community platform shall be in English to promote interoperability and international collaboration.

### Code development
In order to ensure a good working environment for the Community platform all contributors must be  aligned on a GitHub workflow, therefore, all contributors shall follow the GitHub repo strategy: [RepositoryStrategy.md](RepositoryStrategy.md) <br>

<<<<<<<< HEAD:Telemark-120/README.md
In «ElBits Data Standardization» ElBits wants to engage with the DSOs and the vendors to develop and standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. The outcome will be increased reuse of an interface, higher data quality and lower implementation cost for all system applications and interfaces. This again will contribute to more efficient operations and grid development. 

ElBits/DIGIN has developed a test model, the Telemark-120 model for the regional and local distribution grid, that can be used together with the NORDIC44 transmission grid model for the nordic TSO grid. The Telemark-120 model contains the whole grid from the transmission connection to the local end user.

 CGMES v3.0 using CIM17 is the basis for the profiles. CDPSM v2.0 is used as basis for the profiles that are not included in the CGMES v3.0. The Telemark-120 model contains two boundary model profiles, one between each model authority set (MAS). 
========
The [DeveloperGuide](DeveloperGuide.adoc) provides a stepwise instruction of how to make changes to code using Visual Studio Code.

### Issues
Issues are used to plan, discuss and track tasks related to use cases that Elbits_Utility_Standardization is working on.<br>
Issues are also used to report bugs.

### Discussions
GitHub Discussions is used as a communication forum so that users or contributors to Elbits_Utility_Standardization can make suggestions and engage with community members about plans, questions, ideas, and feedback.
>>>>>>>> develop:README.md

Upvote discussions and comments to give higher visibility to topics or ideas you find important or valuable.

|Discussion category| Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
|Announcements      |Updates and news of interest to the user community                                                |
|General            |Anything relevant to Elbits_Utility_Standardization                                               |
|Ideas              |Suggestions to improve Elbits_Utility_Standardization                     |
|Polls              |Used to support decision-making, f.ex. what to prioritize for future code development             |
|Q&A                |Questions and answers to content or implementation of content developed/available on the platform |
|Show and tell      |Provide insight into developed content to support competence enhancement within the user community|

## :mag_right: Navigation
The code repository will be separated into folders based on topics. Below is an overview of the content: 

|Folder name   |Description                                   |
|--------------|----------------------------------------------|
|Code Scripts  |Useful code that was developed for and used to create the DIGIN10 model.|
|DIGIN10       |Develop a test model, the DIGIN10 model, for the Norwegian regional and local distribution grid to standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. Continuation and further development of the DIGIN Grunnprofil project.|

<<<<<<<< HEAD:Telemark-120/README.md
=======
# DIGIN10

## Background

Integrations, exchange of models and data between systems and businesses will become an important and essential process for the energy industry. Today this process is often a based on one to one integrations between systems/applications and ad-hoc solutions. 

In the project «DIGIN CIM grunnprofiler for beregninger og simuleringer i distribusjonsnett» DIGIN wants to engage with the DSOs and the vendors to develop and standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. The outcome will be increased reuse of an interface, higher data quality and lower implementation cost for all system applications and interfaces. This again will contribute to more efficient operations and grid development. 

DIGIN has developed a test model, the DIGIN10 model for the regional and local distribution grid, that can be used together with the NORDIC44 transmission grid model for the nordic TSO grid. The DIGIN10 model contains the whole grid from the transmission connection to the local end user.

 CGMES v3.0 using CIM17 is the basis for the profiles. CDPSM v2.0 is used as basis for the profiles that are not included in the CGMES v3.0. The DIGIN10 model contains two boundary model profiles, one between each model authority set (MAS). 

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

>>>>>>> develop
DIGIN10-30-v2.0 - A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). A release to show the transformation from CGMES v2.4 to CGMES v3.0.

DIGIN10-30-v2.1 -  A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). Including measurement value time series, meter reading time series and necessary asset references.

DIGIN10-30-v2.2 - A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). Including measurement value time series, meter reading time series and necessary asset references. A release that now includes JSON-LD as an alternative to CIMXML.

## Specifications

 A 40 bus power flow case for MV and LV according to CGMES v3.0 (CIM17). Including two Model Authority Sets (MAS), bilateral boundaries and reference data. The solution is done on the merged (MV1+LV1). This version includes measurement values and meter readings to allow power flow calculations based on real time data. The inclusion of measurements will also allow better estimation of future scenarios (steady state values are also based on the real time series).

<<<<<<< HEAD
This version does not include any extensions of the [CGMES v3.0](Telemark-120\docs\StandardReferences.adoc). In [CDPSM v2.0](Telemark-120\docs\StandardReferences.adoc) we have added cim:UsagePoint so that we can model the customer installation. In this version the instance file supporting CDPSM is only added to support cim:UsagePoint and to show how cim:Asset and cim:AssetInfo is connected to the cim:PowerSystemResource. The plan is to show how CGMES + CDPSM can support the Autofos project in upcoming versions. Significant updates have been made to the Equipment Operation (OP) to address cim:Measurement.
=======
This version does not include any extensions of the [CGMES v3.0](DIGIN10\docs\StandardReferences.adoc). In [CDPSM v2.0](DIGIN10\docs\StandardReferences.adoc) we have added cim:UsagePoint so that we can model the customer installation. In this version the instance file supporting CDPSM is only added to support cim:UsagePoint and to show how cim:Asset and cim:AssetInfo is connected to the cim:PowerSystemResource. The plan is to show how CGMES + CDPSM can support the Autofos project in upcoming versions. Significant updates have been made to the Equipment Operation (OP) to address cim:Measurement.
>>>>>>> develop

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

<<<<<<< HEAD
The Telemark-120 model contains the following
=======
The DIGIN10 model contains the following
>>>>>>> develop

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
<<<<<<< HEAD
========
## Versioning
We will use Semantic Versioning as our standard practice for versioning.
Link: [Semantic Versioning 2.0.0](https://semver.org/)
>>>>>>>> develop:README.md
=======
>>>>>>> develop
