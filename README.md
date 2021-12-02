# DIGIN10

## Background

Integrations, exchange of models and data between systems and businesses will become an important and essential process for the energy industry. Today this process is often a based on one to one integrations between systems/applications and ad-hoc solutions. 

In the project «DIGIN CIM grunnprofiler for beregninger og simuleringer i distribusjonsnett» DIGIN wants to engage with the DSOs and the vendors to develop and standardize a set of common profiles for analysis and simulation purposes in tools and systems like SCADA, DMS, NIS and GIS. The outcome will be increased reuse of an interface, higher data quality and lower implementation cost for all system applications and interfaces. This again will contribute to more efficient operations and grid development. 

DIGIN has developed a test model, the DIGIN10 model for the regional and local distribution grid, that can be used together with the NORDIC44 transmission grid model for the nordic TSO grid. The DIGIN10 model contains the whole grid from the transmission connection to the local end user. 

CIM16 and CGMES 2.4 is the basis for the profiles and test model developed and will be available on CIM17 and CGMES 3.0 in the future. The DIGIN10 and NORDIC44 model has a common boundary profile file that contains definitions, classes and attributes that are used across the two adjoining models. 

## Definitions 
- CIM = Common Information Model
- CGMES = Common Grid Model Exchange Standard
- MV = Medium Voltage (in this model: regional and local distribution grid)

## Versions
DIGIN10-24-MV1_v0.5 - First edition of released model
Version v0.5 is for power flow and simulation utilization

## Specifications
CIM16 for MV grid

## Content
The DIGIN10 model contains the following
- profiles according to CIM16/CGMES2.4.15: DL, GL, SV, TP, SSH, EQ
  - All files are CIM.XML files for MV grid
- Boundary profile for interopability with NORDIC44 
- Validation files from CIMDesk
- Drawio images of EQ profile
- png/svg image files of full model from CIMDesk
- NameStandard
- Modeling Guide
