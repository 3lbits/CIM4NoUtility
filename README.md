# DIGIN10

## Background

Integrations, exchange of models and data between systems and businesses will become an important and essential process for the energy industry. Today this process is often a based on one to one integrations between systems/applications and ad-hoc solutions. 

In the project «DIGIN CIM grunnprofiler for beregninger og simuleringer i distribusjonsnett» DIGIN wants to engage with the DSOs and the vendors to develop and standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. The outcome will be increased reuse of an interface, higher data quality and lower implementation cost for all system applications and interfaces. This again will contribute to more efficient operations and grid development. 

DIGIN has developed a test model, the DIGIN10 model for the regional and local distribution grid, that can be used together with the NORDIC44 transmission grid model for the nordic TSO grid. The DIGIN10 model contains the whole grid from the transmission connection to the local end user. 

 CGMES v3.0 using CIM17 is the basis for the profiles. The DIGIN10 model contains two boundary model profiles, one between each model authority sets (MAS).

## Definitions 
- CIM = Common Information Model
- CGMES = Common Grid Model Exchange Standard
- MAS = Model Authority Set
- HV = High Voltage (in this model: transmission grid)
- MV = Medium Voltage (in this model: regional and local distribution grid)
- LV = Low Voltage (in this model: low voltage local distribution grid)


## Versions
DIGIN10-24-v1.0 - Power flow and simulation utilization using CGMES v2.4 (CIM16). 

DIGIN10-30-v2.0 - Conversion of DIGIN10-24-v1.0 to CGMES v3.0 (CIM17).


## Specifications

CGMES v3.0 using CIM17 for MV and LV grid.

## Content
The DIGIN10 model contains the following
- Profiles according to CGMES v3.0 using CIM17: DL, GL, SV, TP, SSH, EQ, OP
  - All files are CIM.XML files
- Customer profiles for both MV and LV according to CDPSM
- Object regestry profiles for LV
- Boundary profiles for interopability with NORDIC44 and between each MAS
- Validation files from CIMdesk
- Drawio images of EQ profile
- png/svg image files of full model from CIMdesk
- Name Standard
- Modeling Guide
- Changelog for Converting to CGMES 3.0 
- Known Issues for current version
