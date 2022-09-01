# DIGIN10

## Background

Integrations, exchange of models and data between systems and businesses will become an important and essential process for the energy industry. Today this process is often a based on one to one integrations between systems/applications and ad-hoc solutions. 

In the project «DIGIN CIM grunnprofiler for beregninger og simuleringer i distribusjonsnett» DIGIN wants to engage with the DSOs and the vendors to develop and standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. The outcome will be increased reuse of an interface, higher data quality and lower implementation cost for all system applications and interfaces. This again will contribute to more efficient operations and grid development. 

DIGIN has developed a test model, the DIGIN10 model for the regional and local distribution grid, that can be used together with the NORDIC44 transmission grid model for the nordic TSO grid. The DIGIN10 model contains the whole grid from the transmission connection to the local end user. 

CIM17 and CGMES 3.0 is the basis for the profiles. The DIGIN10 model contains two boundary model profiles, one between each model authority sets (MAS).

## Definitions 
- CIM = Common Information Model
- CGMES = Common Grid Model Exchange Standard
- MAS = Model Authority Set
- MV = Medium Voltage (in this model: regional and local distribution grid)
- LV = Low Voltage (in this model: low voltage local distribution grid)


## Versions
DIGIN10-24-MV1_v0.5 - First edition of released model - Power flow and simulation utilization using CIM16

DIGIN10-24-v1.0 - Updated model with MV and LV - Power flow and simulation utilization using CIM16

DIGIN10-30-v2.0 - Conversion of DIGIN10-24-v1.0 to CGMES 3.0 using CIM17

## Specifications

CIM17 for MV and LV grid

## Content
The DIGIN10 model contains the following
- Profiles according to CIM17/CGMES3.0: DL, GL, SV, TP, SSH, EQ, OP
  - All files are CIM.XML files
- Customer profiles for both MV and LV according to CDPSM
- Object regestry profiles for LV
- Boundary profiles for interopability with NORDIC44 and between each MAS
- Validation files from CIMDesk
- Drawio images of EQ profile
- png/svg image files of full model from CIMDesk
- Name Standard
- Modeling Guide
- Changelog for Converting to CGMES 3.0 
- Known Issues for current version
