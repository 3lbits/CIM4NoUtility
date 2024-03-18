# NRL to CIM mapping 
## Mast
| NRL |  |  |  |  |  | CIM |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Class/featureType | Attribute | Type | Value | Description | Multiplicity | Class | Attribute | Type | Value | Description | Multiplicity |
| NrlMast |  |  |  |  |  | Structure |  |  |  |  |  |
|  | status | «CodeList» Status |  |  | [1..1] | StructureDeployment | deploymentState | DeploymentStateKind |  |  | [1..1] |
|  |  |  | eksisterende |  |  |  |  |  | installed |  |  |
|  |  |  | fjernet |  |  |  |  |  | removed |  |  |
|  |  |  | planlagtFjernet |  |  |  |  |  | notYetRemoved |  |  |
|  |  |  | planlagtOppført |  |  |  |  |  | notYetInstalled |  |  |
|  | komponentident | CharacterString |  |  | [0..1] | Structure | mRID | String |  | Inherited from cim:IdentifiedObject. Shall be a UUID.  | [1..1] |
|  | navn | CharacterString |  |  | [0..1] | Structure | name | String |  |  | [1..0] |
|  | vertikalAvstand | Real |  | Mandatory to report if hight above ground is >= 15m | [0..1] | Structure | maxHeight | Length |  | The maximum height measured according to "Forskrift om rapportering, registrering og merking av luftfartshinder". If refistered height is the height of "mastens senterhøyde" Structure.height should be used. Length is a CIMDataType with the following attributes: multiplier, unit and value(type:float), if no unit of measure is specified m is the default.  | [1..1] |
|  | luftfartshindermerking | «CodeList» Luftfartshindermerking |  | Mandatory to report if present on 'mast' | [0..1] | OverheadStructure | aviationObstacleMarkingKind | LineMarkingKind |  | LineMarkingKind is an enumeration | [0..1]
|  |  |  | fargemerking |  |  |  |  |  | colourMarking |  |  |
|  |  |  | markør |  |  |  |  |  | marker |  |  |
|  | luftfartshinderlyssetting | «CodeList» Luftfartshinderlyssetting |  | Mandatory to report if present on 'mast' | [0..1] | OverheadStructure | aviationObstacleLightingKind | LineLightingKind |  | LineLightingKind is an enumeration | [0..1] |
|  |  |  | belystMedFlomlys |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | blinkendeHvitt |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | blinkendeRødt |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | fastHvitt |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | fastRødt |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | høyintensitetTypeA |  |  |  |  |  | highIntensityTypeA |  |  |
|  |  |  | høyintensitetTypeB |  |  |  |  |  | highIntensityTypeB |  |  |
|  |  |  | lavintensitetTypeA |  |  |  |  |  | lowIntensityTypeA |  |  |
|  |  |  | lavintensitetTypeB |  |  |  |  |  | lowIntensityTypeB |  |  |
|  |  |  | lyssatt |  |  |  |  |  | lit |  |  |
|  |  |  | mellomintensitetTypeA |  |  |  |  |  | mediumIntesityTypeA |  |  |
|  |  |  | mellomintensitetTypeB |  |  |  |  |  | mediumIntesityTypeB |  |  |
|  |  |  | mellomintensitetTypeC |  |  |  |  |  | mediumIntesityTypeC |  |  |
|  | mastType | «CodeList» MastType |  |  | [1..1] | BaseVoltage | nominalVoltage | Voltage |  | BaseVoltage has a [1..1] to [0..'*'] relation to AssetDeployment. StructureDeployment is child of AssetDeployment and has a [0..1] to [0..1] relation to Structure. Voltage is a CIMDataType with the following attributes: multiplier, unit and value(type:float), if no unit of measure is specified kV is the default. | [1..1] |
|  |  |  | høgspentmast | >1kV |  |  |  |  |  |  |  |
|  |  |  | lavspentmast | <=1kV |  |  |  |  |  |  |  |
|  | verifisertRapporteringsnøyaktighet | «CodeList» VerifisertRapporteringsnøyaktighet |  |  | [1..1] | OverheadStructure | locationMethod | LocationMethodKind |  | the locationMethod attribute is inherited from the Norwegian extension LocationResource which aims to serve the same purpose as PowerSystemResource for non-electrical equipment that is of interest to electrical utilities.| [1..1] |
|  |  |  | 20230101_5-1 |  |  |  |  |  | measured |  |  |
|  |  |  | 0 |  |  |  |  |  |  | if the value of LocationMethodKind is not "measured", i.e. LocationMethodKind.calculated, LocationMethodKind.estimated or LocationMethodKind.manual |  |
|  | høydereferanse | «CodeList» Høydereferanse |  | Mandatory if z coordinate for 'posisjon' is given | [0..1] | n/a |  |  |  | Will only use 'top' for ElBits data exchange. |  |
|  |  |  | fot |  |  |  | n/a |  |  |  |  |
|  |  |  | topp |  |  |  | n/a |  |  |  |  |
|  | posisjon | GM_Point |  | x,y,(z) koordinat (Point) | [1..1] | |  |  |  | will use GeoSPARQL |  |  



## Luftspenn

| NRL |  |  |  |  |  | CIM |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Class/featureType | Attribute | Type | Value | Description | Multiplicity | Class | Attribute | Type | Value | Description | Multiplicity |
| NrlLuftspenn |  |  |  |  |  | ACLineSegmentSpan |  |  |  | Norwegian extension |  |
|  | status | «CodeList» Status |  |  | [1..1] | ACLineSegmentSpanDeployment | deploymentState | DeploymentStateKind |  | Norwegian extension. DeploymentStateKind is an enumeration | [1..1] |
|  |  |  | eksisterende |  |  |  |  |  | installed |  |  |
|  |  |  | fjernet |  |  |  |  |  | removed |  |  |
|  |  |  | planlagtFjernet |  |  |  |  |  | notYetRemoved |  |  |
|  |  |  | planlagtOppført |  |  |  |  |  | notYetInstalled |  |  |
|  | komponentident | CharacterString |  |  | [0..1] | ACLineSegmentSpan | mRID | String |  |  | [1..1] |
|  | navn | CharacterString |  |  | [0..1] | ACLineSegmentSpan | name | String |  |  | [0..1] |
|  | vertikalAvstand | Real |  | Mandatory to report if hight above ground is >= 15m | [0..1] | ACLineSegmentSpan | maxHeight | Length |  | Length is a CIMDataType with the following attributes: multiplier, unit and value(type:float), if no unit of measure is specified m is the default.  | [0..1] |
|  | luftfartshindermerking | «CodeList» Luftfartshindermerking |  | Mandatory to report if present on 'mast' | [0..1] | ACLineSegmentSpan | aviationObstacleMarkingKind | LineMarkingKind |  |  | [0..1] |
|  |  |  | fargeerking |  |  |  |  |  | colourMarking |  |  |
|  |  |  | markør |  |  |  |  |  | marker |  |  |
|  | luftfartshinderlyssetting | «CodeList» Luftfartshinderlyssetting |  | Mandatory to report if present on 'mast' | [0..1] | ACLineSegmentSpan | aviationObstacleLightingKind | LineLightingKind |  |  | [0..1] |
|  |  |  | belystMedFlomlys |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities.|  |
|  |  |  | blinkendeHvitt |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | blinkendeRødt |  |  |  |  |  |  |Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities.  |  |
|  |  |  | fastHvitt |  |  |  |  |  |  |Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities.  |  |
|  |  |  | fastRødt |  |  |  |  |  |  | Not included because it is not specified in "Vedlegg 2" of "Forskrift om rapportering, registrering og merking av luftfartshinder" and to our knowledge is not commonly used by Norwegian electrical utilities. |  |
|  |  |  | høyintensitetTypeA |  |  |  |  |  | highIntesityTypeA |  |  |
|  |  |  | høyintensitetTypeB |  |  |  |  |  | highIntesityTypeB |  |  |
|  |  |  | lavintensitetTypeA |  |  |  |  |  | lowIntesityTypeA |  |  |
|  |  |  | lavintensitetTypeB |  |  |  |  |  | lowIntesityTypeB |  |  |
|  |  |  | lyssatt |  |  |  |  |  | lit |  |  |
|  |  |  | mellomintensitetTypeA |  |  |  |  |  | mediumIntesityTypeA |  |  |
|  |  |  | mellomintensitetTypeB |  |  |  |  |  | mediumIntesityTypeB |  |  |
|  |  |  | mellomintensitetTypeC |  |  |  |  |  | mediumIntesityTypeC |  |  |
|  | luftspennType | «CodeList» LuftspennType |  |  | [1..1] | BaseVoltage | nominalVoltage | Voltage |  | BaseVoltage has a [1..1] to [0..'*'] relation to AssetDeployment. ACLineSegmentSpanDeployment is child of AssetDeployment and has a [0..1] to [0..1] relation to ACLineSegmentSpan. Voltage is a CIMDataType with the following attributes: multiplier, unit and value(type:float), if no unit of measure is specified kV is the default. | [1..1] |
|  |  |  | høgspent | Høgspentlinje, >1kV |  |  |  |  |  |  |  |
|  |  |  | lavspent | Lavspentlinje, <=1kV |  |  |  |  |  |  |  |
|  | anleggsbredde | Real |  | Mandatory to report if width exceeds xx . Det er den bredeste bredden på strekket. Altså bredden mellom de 2 ytterste fasene. | [0..1] | ACLineSegmentSpan | maxWidth | Length |  | Length is a CIMDataType with the following attributes: multiplier, unit and value(type:float), if no unit of measure is specified m is the default. | [0..1] |
|  | verifisertRapporteringsnøyaktighet | «CodeList» VerifisertRapporteringsnøyaktighet |  |  | [1..1] | ACLineSegmentSpan | locationMethod | LocationMethodKind |  | the locationMethod attribute is inherited from the Norwegian extension of PowerSystemResource | [1..1] |
|  |  |  |  | 20230101_5-1 |  |  |  |  | measured |  |  |
|  |  |  |  | 0 |  |  |  |  |  | if the value of LocationMethodKind is not "measured", i.e. LocationMethodKind.calculated, LocationMethodKind.estimated or LocationMethodKind.manual |  | 
|  | høydereferanse | «CodeList» Høydereferanse |  | 	Mandatory if z coordinate for 'beliggenhet' is given | [0..1] | n/a |  |  |  | Will only use 'top' for ElBits data exchange. |  |
|  |  |  | fot |  |  |  | n/a |  |  |  |  |
|  |  |  | topp |  |  |  | n/a |  |  |  |  |
|  | beliggenhet | GM_Curve |  | x,y,(z) koordinater (line) | [1..1] |  |  |  |  | will use GeoSPARQL |  |


## Zone

|  | NRL |  |  |  |  |  | CIM |  |  |  |  |  |  
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Class/featureType | Attribute | Type | Value | Description | Multiplicity | Class | Attribute | Type | Value | Description | Multiplicity |  |  |  |
|  | NrlFlate |  |  |  |  |  | Zone |  |  |  |  |  |  
|  |  | status | «CodeList» Status |  |  | [1..1] | Zone | state | DeploymentStateKind |  | Subject to change.. | [1..1] |  
|  |  |  |  | eksisterende |  |  |  |  |  | installed |  |  |  
|  |  |  |  | fjernet |  |  |  |  |  | removed |  |  |  
|  |  |  |  | planlagtFjernet |  |  |  |  |  | notYetRemoved |  |  |  
|  |  |  |  | planlagtOppført |  |  |  |  |  | notYetInstalled |  |  |  
|  |  | komponentident | CharacterString |  |  | [0..1] | Zone | mRID | String |  |  | [1..1] | 
|  |  | navn | CharacterString |  |  | [0..1] | Zone | name | String |  |  | [0..1]  |  
|  |  | flateType | «CodeList» FlateType |  |  | [1..1] | Zone | zoneKind | ZoneKind |  |  | [1..1]  |  
|  |  |  |  | kontaktledning | Område med høy tetthet av strømførende luftspenn som er spent over sporet til en jernbane-, forstadsbane- eller sporvogns-trasé. |  |  |  |  | electricalNetwork | Suggest to either use ZoneKind.electricalNetwork or extend ZoneKind|  |  
|  |  |  |  | trafostasjon |  |  |  |  |  | substation | norwegian extension |  |  
|  |  | verifisertRapporteringsNøyaktighet | «CodeList» VerifisertRapporteringsnøyaktighet |  |  | [1..1] | Zone | locationMethod | LocationMethodKind |  | the locationMethod attribute is inherited from the Norwegian extension LocationResource which aims to serve the same purpose as PowerSystemResource for non-electrical equipment that is of interest to electrical utilities.| [1..1] |
|  |  |  |  | 20230101_5-1 |  |  |  |  |  | measured |  |  |
|  |  |  |  | 0 |  |  |  |  |  |  | if the value of LocationMethodKind is not "measured", i.e. LocationMethodKind.calculated, LocationMethodKind.estimated or LocationMethodKind.manual |  |  
|  |  | høydereferanse | «CodeList» Høydereferanse |  | 	Mandatory if z coordinate for 'område' is given | [0..1] | n/a |  |  | Will only use 'top' for ElBits data exchange. |  |
|  |  |  | fot |  |  |  |  | n/a |  |  |  |
|  |  |  | topp |  |  |  |  | n/a |  |  |  |
|  |  | område | GM_Surface |  | x,y,(z) koordinater (polygon) | [1..1] |  |  |  |  | will use GeoSPARQL |  |