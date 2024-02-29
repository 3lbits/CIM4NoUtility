# NRL to CIM mapping 
## Mast
| NRL |  |  |  |  |  | CIM |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Class/featureType | Attribute | Type | Value | Description | Multiplicity | Class | Attribute | Type | Value | Description | Multiplicity |
| NrlMast |  |  |  |  |  | Structure |  |  |  |  |  |
|  | status | «CodeList» Status |  |  | [1..1] | AssetDeployment | deploymentState | DeploymentStateKind |  | Might use a specialized class of AssetDeployment, e.g. StructureDeployment. AssetDeployment has a [0..1] to [0..1] relation to Structure. | [1..1] |
|  |  |  | eksisterende |  |  |  |  |  | installed |  |  |
|  |  |  | fjernet |  |  |  |  |  | removed |  |  |
|  |  |  | planlagtFjernet |  |  |  |  |  |  |  |  |
|  |  |  | planlagtOppført |  |  |  |  |  | notYetInstalled |  |  |
|  | komponentident | CharacterString |  |  | [0..1] | Structure | mRID | String |  | Inherited from cim:IdentifiedObject. Shall be a UUID.  | [1..1] |
|  | navn | CharacterString |  |  | [0..1] | Structure | name | String |  |  | [1..0] |
|  | vertikalAvstand | Real |  | Mandatory to report if hight above ground is >= 15m | [0..1] | Structure | height | Length |  | Will be the height of "mastens senterhøyde". Might extend Structure with Structure.maxHeight to support reporting of actual 'vertikal avstand' according to NRL standards | [0..1] |
|  | luftfartshindermerking | «CodeList» Luftfartshindermerking |  | Mandatory to report if present on 'mast' | [0..1] |  |  |  |  | Structure.aviationObstacleMarkingKind? |  |
|  |  |  | fargemerking |  |  |  |  |  |  |  |  |
|  |  |  | markør |  |  |  |  |  |  |  |  |
|  | luftfartshinderlyssetting | «CodeList» Luftfartshinderlyssetting |  | Mandatory to report if present on 'mast' | [0..1] |  |  |  |  | Structure.aviationObstacleLightingKind? |  |
|  |  |  | belystMedFlomlys |  |  |  |  |  |  |  |  |
|  |  |  | blinkendeHvitt |  |  |  |  |  |  |  |  |
|  |  |  | blinkendeRødt |  |  |  |  |  |  |  |  |
|  |  |  | fastHvitt |  |  |  |  |  |  |  |  |
|  |  |  | fastRødt |  |  |  |  |  |  |  |  |
|  |  |  | høyintensitetTypeA |  |  |  |  |  |  |  |  |
|  |  |  | høyintensitetTypeB |  |  |  |  |  |  |  |  |
|  |  |  | lavintensitetTypeA |  |  |  |  |  |  |  |  |
|  |  |  | lavintensitetTypeB |  |  |  |  |  |  |  |  |
|  |  |  | lyssatt |  |  |  |  |  |  |  |  |
|  |  |  | mellomintensitetTypeA |  |  |  |  |  |  |  |  |
|  |  |  | mellomintensitetTypeB |  |  |  |  |  |  |  |  |
|  |  |  | mellomintensitetTypeC |  |  |  |  |  |  |  |  |
|  | mastType | «CodeList» MastType |  |  | [1..1] | BaseVoltage | nominalVoltage | Voltage |  | BaseVoltage has a [1..1] to [0..'*'] relation to AssetDeployment. AssetDeployment has a [0..1] to [0..1] relation to Structure. Voltage is a CIMDataType with the following attributes: multiplier, unit and value(type:float), if no unit of measure is specified kV is the default. | [1..1] |
|  |  |  | høgspentmast | >1kV |  |  |  |  |  |  |  |
|  |  |  | lavspentmast | <=1kV |  |  |  |  |  |  |  |
|  | verifisertRapporteringsnøyaktighet | «CodeList» VerifisertRapporteringsnøyaktighet |  |  | [1..1] |  |  |  |  | cim:Location or geo:hasSpacialAccuracy? Needs more discussion for mapping. |  |
|  |  |  | 20230101_5-1 |  |  |  |  |  |  |  |  |
|  |  |  | 0 |  |  |  |  |  |  |  |  |
|  | høydereferanse | «CodeList» Høydereferanse |  | Mandatory if z coordinate for 'posisjon' is given | [0..1] | n/a |  |  |  | Will only use 'top' for ElBits data exchange. |  |
|  |  |  | fot |  |  |  | n/a |  |  |  |  |
|  |  |  | topp |  |  |  | n/a |  |  |  |  |
|  | posisjon | GM_Point |  | x,y,(z) koordinat (Point) | [1..1] | PositionPoint |  |  |  | Relation. Structure.Location.PositionPoint. Structure has a [0..'*'] to [0..1] Location. Location has a [1..1] to [0..'*'] relation to PositionPoint | [1..1] |
|  |  |  |  |  |  |  | xPosition | X axis position. |  |  | [1..1] |
|  |  |  |  |  |  |  | yPosition | Y axis position. |  |  | [1..1] |
|  |  |  |  |  |  |  | zPosition | Z axis position. |  |  | [1..0] |


## Luftspenn

| NRL |  |  |  |  |  | CIM |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Class/featureType | Attribute | Type | Value | Description | Multiplicity | Class | Attribute | Type | Value | Description | Multiplicity |
| NrlLuftspenn |  |  |  |  |  | ACLineSegmentSpan |  |  |  | Norwegian extension |  |
|  | status | «CodeList» Status |  |  | [1..1] |  |  |  |  | suggest to extend model with a specialization of AssetDeployment, e.g. LineDeployment |  |
|  |  |  | eksisterende |  |  |  |  |  |  |  |  |
|  |  |  | fjernet |  |  |  |  |  |  |  |  |
|  |  |  | planlagtFjernet |  |  |  |  |  |  |  |  |
|  |  |  | planlagtOppført |  |  |  |  |  |  |  |  |
|  | komponentident | CharacterString |  |  | [0..1] | ACLineSegmentSpan | mRID | String |  |  | [1..1] |
|  | navn | CharacterString |  |  | [0..1] | ACLineSegmentSpan | name | String |  |  | [0..1] |
|  | vertikalAvstand | Real |  | Mandatory to report if hight above ground is >= 15m | [0..1] | ACLineSegmentSpan | maxHeight | Length |  |  | [0..1] |
|  | luftfartshindermerking | «CodeList» Luftfartshindermerking |  | Mandatory to report if present on 'mast' | [0..1] | ACLineSegmentSpan | aviationObstacleMarkingKind | LineMarkingKind |  |  | [0..1] |
|  |  |  | fargeerking |  |  |  |  |  | colourMarking |  |  |
|  |  |  | markør |  |  |  |  |  | marker |  |  |
|  |  |  |  |  |  |  |  |  | none |  |  |
|  | luftfartshinderlyssetting | «CodeList» Luftfartshinderlyssetting |  | Mandatory to report if present on 'mast' | [0..1] | ACLineSegmentSpan | aviationObstacleLightingKind | LineLightingKind |  |  | [0..1] |
|  |  |  | belystMedFlomlys |  |  |  |  |  |  |  |  |
|  |  |  | blinkendeHvitt |  |  |  |  |  |  |  |  |
|  |  |  | blinkendeRødt |  |  |  |  |  |  |  |  |
|  |  |  | fastHvitt |  |  |  |  |  |  |  |  |
|  |  |  | fastRødt |  |  |  |  |  |  |  |  |
|  |  |  | høyintensitetTypeA |  |  |  |  |  |  |  |  |
|  |  |  | høyintensitetTypeB |  |  |  |  |  |  |  |  |
|  |  |  | lavintensitetTypeA |  |  |  |  |  |  |  |  |
|  |  |  | lavintensitetTypeB |  |  |  |  |  |  |  |  |
|  |  |  | lyssatt |  |  |  |  |  | lit |  |  |
|  |  |  | mellomintensitetTypeA |  |  |  |  |  | mediumIntesityTypeA |  |  |
|  |  |  | mellomintensitetTypeB |  |  |  |  |  | mediumIntesityTypeB |  |  |
|  |  |  | mellomintensitetTypeC |  |  |  |  |  | mediumIntesityTypeC |  |  |
|  |  |  |  |  |  |  |  |  | none |  |  |
|  | luftspennType | «CodeList» LuftspennType |  |  | [1..1] |  |  |  |  | suggest to extend model with a specialization of AssetDeployment, e.g. LineDeployment, should then use BaseVoltage relation to AssetDeployment to specify voltage level | [1..1] |
|  |  |  | høgspent | Høgspentlinje, >1kV |  |  |  |  |  |  |  |
|  |  |  | lavspent | Lavspentlinje, <=1kV |  |  |  |  |  |  |  |
|  | anleggsbredde | Real |  | Mandatory to report if width exceeds xx . Det er den bredeste bredden på strekket. Altså bredden mellom de 2 ytterste fasene. | [0..1] |  |  |  |  | add attribute ACLineSegmentSpan.maxWidth  | [0..1] |
|  | verifisertRapporteringsnøyaktighet | «CodeList» VerifisertRapporteringsnøyaktighet |  |  |  |  |  |  |  | cim:Location or geo:hasSpacialAccuracy? Needs more discussion for mapping. |  |
|  | høydereferanse | «CodeList» Høydereferanse |  | 	Mandatory if z coordinate for 'beliggenhet' is given |  | n/a |  |  |  | Will only use 'top' for ElBits data exchange. |  |
|  |  |  | fot |  |  |  | n/a |  |  |  |  |
|  |  |  | topp |  |  |  | n/a |  |  |  |  |
|  | beliggenhet | GM_Curve |  | x,y,(z) koordinater (line) | [1..1] | PositionPoint |  |  |  | Relation: ACLineSegmentSpan.Location.PositionPoint | [1..1] |
|  |  |  |  |  |  |  | xPosition |  |  | x axis position. | [1..1] |
|  |  |  |  |  |  |  | yPosition |  |  | Y axis position. | [1..1] |
|  |  |  |  |  |  |  | zPosition |  |  | Z axis position. | [0..1] |


## Zone

|  | NRL |  |  |  |  |  | CIM |  |  |  |  |  |  
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Class/featureType | Attribute | Type | Value | Description | Multiplicity | Class | Attribute | Type | Value | Description | Multiplicity |  |  |  |
|  | NrlFlate |  |  |  |  |  | Zone |  |  |  |  |  |  
|  |  | status | «CodeList» Status |  |  | [1..1] |  |  |  |  |  |  |  
|  |  |  |  | eksisterende |  |  |  |  |  |  |  |  |  
|  |  |  |  | fjernet |  |  |  |  |  |  |  |  |  
|  |  |  |  | planlagtFjernet |  |  |  |  |  |  |  |  |  
|  |  |  |  | planlagtOppført |  |  |  |  |  |  |  |  |  
|  |  | komponentident | CharacterString |  |  | [0..1] | Zone | mRID | String |  |  | [1..1] | 
|  |  | navn | CharacterString |  |  | [0..1] | Zone | name | String |  |  | [0..1]  |  
|  |  | flateType | «CodeList» FlateType |  |  | [1..1] | Zone | kind |  |  |  | [1..1]  |  
|  |  |  |  | kontaktledning | Område med høy tetthet av strømførende luftspenn som er spent over sporet til en jernbane-, forstadsbane- eller sporvogns-trasé. |  |  |  |  |  | Suggest to either use ZoneKind.electricalNetwork or extend ZoneKind|  |  
|  |  |  |  | trafostasjon |  |  |  |  |  |  | Suggest to extend ZoneKind.substation, and either use ZoneKind.electricalNetwork  |  |  
|  |  | verifisertRapporteringsNøyaktighet | «CodeList» VerifisertRapporteringsnøyaktighet |  |  | [1..1] |  |  |  |  |  |  |  
|  |  | høydereferanse | «CodeList» Høydereferanse |  | 	Mandatory if z coordinate for 'område' is given |  | n/a |  |  | Will only use 'top' for ElBits data exchange. |  |
|  |  |  | fot |  |  |  |  | n/a |  |  |  |
|  |  |  | topp |  |  |  |  | n/a |  |  |  |
|  |  | område | GM_Surface |  | x,y,(z) koordinater (polygon) | [1..1] | PositionPoint |  |  |  | PositionPoint has a [0..*] to [1..1] relation to Zone | [1..1]  | 
|  |  |  |  |  |  |  |  | xPosition |  |  | X axis position. |  |  
|  |  |  |  |  |  |  |  | yPosition |  |  | Y axis position. |  |  
|  |  |  |  |  |  |  |  | zPosition |  |  | Z axis position. |  |  
