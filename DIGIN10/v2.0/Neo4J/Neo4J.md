# Using Neo4J for importing DIGIN Grunnprofil

This is made for sharing what Digin Grunnprofil have made for importing .xml files into Neo4J with cypher. The reason for making this is to have a visual method to check quality errors in conductivity.

**DIGIN can not take any responsibillity for errors in using this code.**
**This document does not include setup of Neo4J or apoc**

## Classes

- ACLineSegment
- (BaseVoltage)
- Bay
- Breaker
- BusbarSection
- ConnectivityNode
- ControlArea
- CurrentLimit
- Disconnector
- EquivalentInjection
- Feeder
- (GeographicalRegion)
- Line
- LinearShuntCompensator
- LoadArea
- LoadBreakSwitch
- OperationalLimitSet
- OperationalLimitType
- PowerTransformer
- PowerTransformerEnd
- RatioTapChanger
- (SubGeographicalRegion)
- SubLoadArea
- Substation
- TapChangerControl
- Terminal
- VoltageLevel

## Cypher Code

CALL apoc.load.xml("your chosen file")

Example:

- DIGIN10-24-LV1_EQ.xml
- DIGIN10-24-MV1_EQ.xml

### Conducting

#### ACLineSegment

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ACLineSegment"] AS ACLineSegments
WITH ACLineSegments
UNWIND ACLineSegments AS ACLineSegment
WITH ACLineSegment.`rdf:ID` AS `rdf:ID`,
	 [item in ACLineSegment._children WHERE item._type = "PowerSystemResource.PSRType"][0] AS PSRType,
	 [item in ACLineSegment._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in ACLineSegment._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ACLineSegment._children WHERE item._type = "Conductor.length"][0] AS length,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.b0ch"][0] AS b0ch,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.bch"][0] AS bch,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.r"][0] AS r,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.r0"][0] AS r0,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.x"][0] AS x,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.x0"][0] AS x0,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.shortCircuitEndTemperature"][0] AS shortCircuitEndTemperature

MERGE (m:ACLineSegment {`rdf:ID`: `rdf:ID`})
SET
m.PSRType = substring(PSRType.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.name = name._text,
m.length = length._text,
m.b0ch = b0ch._text,
m.bch = bch._text,
m.r = r._text,
m.r0 = r0._text,
m.x = x._text,
m.x0 = x0._text,
m.shortCircuitEndTemperature = shortCircuitEndTemperature._text
;
```

#### BusbarSection

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "BusbarSection"] AS BusbarSections
WITH BusbarSections
UNWIND BusbarSections AS BusbarSection
WITH BusbarSection.`rdf:ID` AS `rdf:ID`,
	 [item in BusbarSection._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in BusbarSection._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in BusbarSection._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:BusbarSection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

#### ConformLoad

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ConformLoad"] AS ConformLoads
WITH ConformLoads
UNWIND ConformLoads AS ConformLoad
WITH ConformLoad.`rdf:ID` AS `rdf:ID`,
	 [item in ConformLoad._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ConformLoad._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in ConformLoad._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:ConformLoad {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

#### ConnectivityNode

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ConnectivityNode"] AS ConnectivityNodes
WITH ConnectivityNodes
UNWIND ConnectivityNodes AS ConnectivityNode
WITH ConnectivityNode.`rdf:ID` AS `rdf:ID`,
	 [item in ConnectivityNode._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ConnectivityNode._children WHERE item._type = "ConnectivityNode.ConnectivityNodeContainer"][0] AS ConnectivityNodeContainer

MERGE (m:ConnectivityNode {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.ConnectivityNodeContainer = substring(ConnectivityNodeContainer.`rdf:resource`, 1)
;
```

#### EquivalentInjection

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "EquivalentInjection"] AS EquivalentInjections
WITH EquivalentInjections
UNWIND EquivalentInjections AS EquivalentInjection
WITH EquivalentInjection.`rdf:ID` AS `rdf:ID`,
	 [item in EquivalentInjection._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in EquivalentInjection._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer,
	 [item in EquivalentInjection._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage

MERGE (m:EquivalentInjection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1)
;
```

#### ExternalNetworkInjection

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ExternalNetworkInjection"] AS ExternalNetworkInjections
WITH ExternalNetworkInjections
UNWIND ExternalNetworkInjections AS ExternalNetworkInjection
WITH ExternalNetworkInjection.`rdf:ID` AS `rdf:ID`,
	 [item in ExternalNetworkInjection._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.maxInitialSymShCCurren"][0] AS maxInitialSymShCCurren,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.minInitialSymShCCurrent"][0] AS minInitialSymShCCurrent,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.maxR1ToX1Ratio"][0] AS maxR1ToX1Ratio,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.voltageFactor"][0] AS voltageFactor,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage

MERGE (m:ExternalNetworkInjection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.maxInitialSymShCCurren = maxInitialSymShCCurren._text,
m.minInitialSymShCCurrent = minInitialSymShCCurrent._text,
m.maxR1ToX1Ratio = maxR1ToX1Ratio._text,
m.voltageFactor = voltageFactor._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1)
;
```

#### PowerTransformer

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PowerTransformer"] AS PowerTransformers
WITH PowerTransformers
UNWIND PowerTransformers AS PowerTransformer
WITH PowerTransformer.`rdf:ID` AS `rdf:ID`,
	 [item in PowerTransformer._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in PowerTransformer._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:PowerTransformer {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

#### Switch

#### Breaker

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Breaker"] AS Breakers
WITH Breakers
UNWIND Breakers AS Breaker
WITH Breaker.`rdf:ID` AS `rdf:ID`,
	 [item in Breaker._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Breaker._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Breaker._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Breaker {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

##### Disconnector

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Disconnector"] AS Disconnectors
WITH Disconnectors
UNWIND Disconnectors AS Disconnector
WITH Disconnector.`rdf:ID` AS `rdf:ID`,
	 [item in Disconnector._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Disconnector._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Disconnector._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Disconnector {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

##### Fuse

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Fuse"] AS Fuses
WITH Fuses
UNWIND Fuses AS Fuse
WITH Fuse.`rdf:ID` AS `rdf:ID`,
	 [item in Fuse._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Fuse._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Fuse._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Fuse {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

##### LoadBreakSwitch

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "LoadBreakSwitch"] AS LoadBreakSwitchs
WITH LoadBreakSwitchs
UNWIND LoadBreakSwitchs AS LoadBreakSwitch
WITH LoadBreakSwitch.`rdf:ID` AS `rdf:ID`,
	 [item in LoadBreakSwitch._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in LoadBreakSwitch._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in LoadBreakSwitch._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:LoadBreakSwitch {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

#### Terminal

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Terminal"] AS Terminals
WITH Terminals
UNWIND Terminals AS Terminal
WITH Terminal.`rdf:ID` AS `rdf:ID`,
	 [item in Terminal._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Terminal._children WHERE item._type = "ACDCTerminal.sequenceNumber"][0] AS sequenceNumber,
	 [item in Terminal._children WHERE item._type = "Terminal.ConnectivityNode"][0] AS ConnectivityNode,
	 [item in Terminal._children WHERE item._type = "Terminal.ConductingEquipment"][0] AS ConductingEquipment

MERGE (m:Terminal {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.sequenceNumber = sequenceNumber._text,
m.ConnectivityNode = substring(ConnectivityNode.`rdf:resource`, 1),
m.ConductingEquipment = substring(ConductingEquipment.`rdf:resource`, 1)
;
```

#### StationSupply

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "StationSupply"] AS StationSupplys
WITH StationSupplys
UNWIND StationSupplys AS StationSupply
WITH StationSupply.`rdf:ID` AS `rdf:ID`,
	 [item in StationSupply._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in StationSupply._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in StationSupply._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:StationSupply {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;
```

### Non Conducting

#### BaseVoltage

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "BaseVoltage"] AS BaseVoltages
WITH BaseVoltages
UNWIND BaseVoltages AS BaseVoltage
WITH BaseVoltage.`rdf:ID` AS `rdf:ID`,
	 [item in BaseVoltage._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in BaseVoltage._children WHERE item._type = "BaseVoltage.nominalVoltage"][0] AS nominalVoltage

MERGE (m:BaseVoltage {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.nominalVoltage = nominalVoltage._text
;
```

#### Bay

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Bay"] AS Bays
WITH Bays
UNWIND Bays AS Bay
WITH Bay.`rdf:ID` AS `rdf:ID`,
	 [item in Bay._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Bay._children WHERE item._type = "Bay.VoltageLevel"][0] AS VoltageLevel,
	 [item in Bay._children WHERE item._type = "Bay.Substation"][0] AS Substation

MERGE (m:Bay {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.VoltageLevel = substring(VoltageLevel.`rdf:resource`, 1),
m.Substation = substring(Substation.`rdf:resource`, 1)
;
```

#### PowerTransformerEnd

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PowerTransformerEnd"] AS PowerTransformerEnds
WITH PowerTransformerEnds
UNWIND PowerTransformerEnds AS PowerTransformerEnd
WITH PowerTransformerEnd.`rdf:ID` AS `rdf:ID`,
	 [item in PowerTransformerEnd._children WHERE item._type = "IdentifiedObject.name"][0] AS name, 
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.endNumber"][0] AS endNumber,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.ratedU"][0] AS ratedU,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.ratedS"][0] AS ratedS,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.r"][0] AS r,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.x"][0] AS x,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.r0"][0] AS r0,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.x0"][0] AS x0,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.b"][0] AS b,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.PowerTransformer"][0] AS PowerTransformer,
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.Terminal"][0] AS Terminal,
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.BaseVoltage"][0] AS BaseVoltage

MERGE (m:PowerTransformerEnd {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.endNumber = endNumber._text,
m.ratedU = ratedU._text,
m.ratedS = ratedS._text,
m.r = r._text,
m.x = x._text,
m.r0 = r0._text,
m.x0 = x0._text,
m.b = b._text,
m.PowerTransformer = substring(PowerTransformer.`rdf:resource`, 1),
m.Terminal = substring(Terminal.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1)
;
```

#### PSRType

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PSRType"] AS PSRTypes
WITH PSRTypes
UNWIND PSRTypes AS PSRType
WITH PSRType.`rdf:ID` AS `rdf:ID`,
	 [item in PSRType._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:PSRType {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;
```

#### RatioTapChanger

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "RatioTapChanger"] AS RatioTapChangers
WITH RatioTapChangers
UNWIND RatioTapChangers AS RatioTapChanger
WITH RatioTapChanger.`rdf:ID` AS `rdf:ID`,
	 [item in RatioTapChanger._children WHERE item._type = "IdentifiedObject.name"][0] AS name, 
	 [item in RatioTapChanger._children WHERE item._type = "RatioTapChanger.stepVoltageIncrement"][0] AS stepVoltageIncrement,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.highStep"][0] AS highStep,
	 [item in RatioTapChanger._children WHERE item._type = "RatioTapChanger.tculControlMode"][0] AS tculControlMode,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.lowStep"][0] AS lowStep,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.ltcFlag"][0] AS ltcFlag,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.neutralStep"][0] AS neutralStep,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.neutralU"][0] AS neutralU,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.normalStep"][0] AS normalStep,
	 [item in RatioTapChanger._children WHERE item._type = "RatioTapChanger.TransformerEnd"][0] AS TransformerEnd

MERGE (m:RatioTapChanger {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.stepVoltageIncrement = stepVoltageIncrement._text,
m.tculControlMode = tculControlMode._text,
m.highStep = highStep._text,
m.lowStep = lowStep._text,
m.ltcFlag = ltcFlag._text,
m.neutralStep = neutralStep._text,
m.neutralU = neutralU._text,
m.normalStep = normalStep._text,
m.TransformerEnd = substring(TransformerEnd.`rdf:resource`, 1)
;
```

#### SubGeographicalRegion

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "SubGeographicalRegion"] AS SubGeographicalRegions
WITH SubGeographicalRegions
UNWIND SubGeographicalRegions AS SubGeographicalRegion
WITH SubGeographicalRegion.`rdf:ID` AS `rdf:ID`,
	 [item in SubGeographicalRegion._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in SubGeographicalRegion._children WHERE item._type = "IdentifiedObject.description"][0] AS description

MERGE (m:SubGeographicalRegion {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.description = description._text
;
```

#### Substation

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Substation"] AS Substations
WITH Substations
UNWIND Substations AS Substation
WITH Substation.`rdf:ID` AS `rdf:ID`,
	 [item in Substation._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Substation._children WHERE item._type = "IdentifiedObject.description"][0] AS description,
	 [item in Substation._children WHERE item._type = "PowerSystemResource.PSRType"][0] AS PSRType,
	 [item in Substation._children WHERE item._type = "Substation.SubGeographicalRegion"][0] AS SubGeographicalRegion

MERGE (m:Substation {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.description = description._text,
m.PSRType = substring(PSRType.`rdf:resource`, 1),
m.SubGeographicalRegion = substring(SubGeographicalRegion.`rdf:resource`, 1)
;
```

#### VoltageLevel

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "VoltageLevel"] AS VoltageLevels
WITH VoltageLevels
UNWIND VoltageLevels AS VoltageLevel
WITH VoltageLevel.`rdf:ID` AS `rdf:ID`,
	 [item in VoltageLevel._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in VoltageLevel._children WHERE item._type = "VoltageLevel.BaseVoltage"][0] AS BaseVoltage,
	 [item in VoltageLevel._children WHERE item._type = "VoltageLevel.Substation"][0] AS Substation

MERGE (m:VoltageLevel {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.Substation = substring(Substation.`rdf:resource`, 1)
;
```

#### UsagePoint

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "UsagePoint"] AS UsagePoints
WITH UsagePoints
UNWIND UsagePoints AS UsagePoint
WITH UsagePoint.`rdf:ID` AS `rdf:ID`,
	 [item in UsagePoint._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in UsagePoint._children WHERE item._type = "UsagePoint.Equipments"][0] AS Equipments

MERGE (m:UsagePoint {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.Equipments = 	substring(Equipments.`rdf:resource`, 1)
;
```

#### CurrentLimit

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "CurrentLimit"] AS CurrentLimits
WITH CurrentLimits
UNWIND CurrentLimits AS CurrentLimit
WITH CurrentLimit.`rdf:ID` AS `rdf:ID`,
	 [item in CurrentLimit._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in CurrentLimit._children WHERE item._type = "CurrentLimit.value"][0] AS value,
	 [item in CurrentLimit._children WHERE item._type = "OperationalLimit.OperationalLimitSet"][0] AS OperationalLimitSet,
	 [item in CurrentLimit._children WHERE item._type = "OperationalLimit.OperationalLimitType"][0] AS OperationalLimitType

MERGE (m:CurrentLimit {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.value = value._text,
m.OperationalLimitSet = substring(OperationalLimitSet.`rdf:resource`, 1),
m.OperationalLimitType = substring(OperationalLimitType.`rdf:resource`, 1)
;
```

#### OperationalLimitSet

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "OperationalLimitSet"] AS OperationalLimitSets
WITH OperationalLimitSets
UNWIND OperationalLimitSets AS OperationalLimitSet
WITH OperationalLimitSet.`rdf:ID` AS `rdf:ID`,
	 [item in OperationalLimitSet._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in OperationalLimitSet._children WHERE item._type = "IdentifiedObject.description"][0] AS description,
	 [item in OperationalLimitSet._children WHERE item._type = "OperationalLimitSet.Terminal"][0] AS Terminal

MERGE (m:OperationalLimitSet {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.description = description._text,
m.Terminal = substring(Terminal.`rdf:resource`, 1)
;
```

#### OperationalLimitType

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "OperationalLimitType"] AS OperationalLimitTypes
WITH OperationalLimitTypes
UNWIND OperationalLimitTypes AS OperationalLimitType
WITH OperationalLimitType.`rdf:ID` AS `rdf:ID`,
	 [item in OperationalLimitType._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in OperationalLimitType._children WHERE item._type = "OperationalLimitType.acceptableDuration"][0] AS acceptableDuration

MERGE (m:OperationalLimitType {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.acceptableDuration = acceptableDuration._text
;
```

### Define Relations

```cypher
MATCH (n), (b) WHERE n.PSRType = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.BaseVoltage = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.EquipmentContainer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.PowerTransformer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.Terminal = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.TransformerEnd = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.ConnectivityNode = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.ConductingEquipment = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.Equipments = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.Substation = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.SubGeographicalRegion = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.VoltageLevel = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.OperationalLimitSet = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.OperationalLimitType = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.ConnectivityNodeContainer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);
```

### Total Script

```cypher
CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ACLineSegment"] AS ACLineSegments
WITH ACLineSegments
UNWIND ACLineSegments AS ACLineSegment
WITH ACLineSegment.`rdf:ID` AS `rdf:ID`,
	 [item in ACLineSegment._children WHERE item._type = "PowerSystemResource.PSRType"][0] AS PSRType,
	 [item in ACLineSegment._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in ACLineSegment._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ACLineSegment._children WHERE item._type = "Conductor.length"][0] AS length,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.b0ch"][0] AS b0ch,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.bch"][0] AS bch,
     [item in ACLineSegment._children WHERE item._type = "ACLineSegment.r"][0] AS r,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.r0"][0] AS r0,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.x"][0] AS x,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.x0"][0] AS x0,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.shortCircuitEndTemperature"][0] AS shortCircuitEndTemperature

MERGE (m:ACLineSegment {`rdf:ID`: `rdf:ID`})
SET
m.PSRType = substring(PSRType.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.name = name._text,
m.length = length._text,
m.b0ch = b0ch._text,
m.bch = bch._text,
m.r = r._text,
m.r0 = r0._text,
m.x = x._text,
m.x0 = x0._text,
m.shortCircuitEndTemperature = shortCircuitEndTemperature._text
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "BaseVoltage"] AS BaseVoltages
WITH BaseVoltages
UNWIND BaseVoltages AS BaseVoltage
WITH BaseVoltage.`rdf:ID` AS `rdf:ID`,
	 [item in BaseVoltage._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in BaseVoltage._children WHERE item._type = "BaseVoltage.nominalVoltage"][0] AS nominalVoltage

MERGE (m:BaseVoltage {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.nominalVoltage = nominalVoltage._text
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Bay"] AS Bays
WITH Bays
UNWIND Bays AS Bay
WITH Bay.`rdf:ID` AS `rdf:ID`,
	 [item in Bay._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Bay._children WHERE item._type = "Bay.VoltageLevel"][0] AS VoltageLevel,
	 [item in Bay._children WHERE item._type = "Bay.Substation"][0] AS Substation

MERGE (m:Bay {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.VoltageLevel = substring(VoltageLevel.`rdf:resource`, 1),
m.Substation = substring(Substation.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "BusbarSection"] AS BusbarSections
WITH BusbarSections
UNWIND BusbarSections AS BusbarSection
WITH BusbarSection.`rdf:ID` AS `rdf:ID`,
	 [item in BusbarSection._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in BusbarSection._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in BusbarSection._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:BusbarSection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ConformLoad"] AS ConformLoads
WITH ConformLoads
UNWIND ConformLoads AS ConformLoad
WITH ConformLoad.`rdf:ID` AS `rdf:ID`,
	 [item in ConformLoad._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ConformLoad._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in ConformLoad._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:ConformLoad {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ConnectivityNode"] AS ConnectivityNodes
WITH ConnectivityNodes
UNWIND ConnectivityNodes AS ConnectivityNode
WITH ConnectivityNode.`rdf:ID` AS `rdf:ID`,
	 [item in ConnectivityNode._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ConnectivityNode._children WHERE item._type = "ConnectivityNode.ConnectivityNodeContainer"][0] AS ConnectivityNodeContainer

MERGE (m:ConnectivityNode {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.ConnectivityNodeContainer = substring(ConnectivityNodeContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ExternalNetworkInjection"] AS ExternalNetworkInjections
WITH ExternalNetworkInjections
UNWIND ExternalNetworkInjections AS ExternalNetworkInjection
WITH ExternalNetworkInjection.`rdf:ID` AS `rdf:ID`,
	 [item in ExternalNetworkInjection._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.maxInitialSymShCCurren"][0] AS maxInitialSymShCCurren,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.minInitialSymShCCurrent"][0] AS minInitialSymShCCurrent,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.maxR1ToX1Ratio"][0] AS maxR1ToX1Ratio,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ExternalNetworkInjection.voltageFactor"][0] AS voltageFactor,
	 [item in ExternalNetworkInjection._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage

MERGE (m:ExternalNetworkInjection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.maxInitialSymShCCurren = maxInitialSymShCCurren._text,
m.minInitialSymShCCurrent = minInitialSymShCCurrent._text,
m.maxR1ToX1Ratio = maxR1ToX1Ratio._text,
m.voltageFactor = voltageFactor._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Fuse"] AS Fuses
WITH Fuses
UNWIND Fuses AS Fuse
WITH Fuse.`rdf:ID` AS `rdf:ID`,
	 [item in Fuse._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Fuse._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Fuse._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Fuse {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "LoadBreakSwitch"] AS LoadBreakSwitchs
WITH LoadBreakSwitchs
UNWIND LoadBreakSwitchs AS LoadBreakSwitch
WITH LoadBreakSwitch.`rdf:ID` AS `rdf:ID`,
	 [item in LoadBreakSwitch._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in LoadBreakSwitch._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in LoadBreakSwitch._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:LoadBreakSwitch {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Disconnector"] AS Disconnectors
WITH Disconnectors
UNWIND Disconnectors AS Disconnector
WITH Disconnector.`rdf:ID` AS `rdf:ID`,
	 [item in Disconnector._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Disconnector._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Disconnector._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Disconnector {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "SynchronousMachine"] AS SynchronousMachines
WITH SynchronousMachines
UNWIND SynchronousMachines AS SynchronousMachine
WITH SynchronousMachine.`rdf:ID` AS `rdf:ID`,
	 [item in SynchronousMachine._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:SynchronousMachine {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "LinearShuntCompensator"] AS LinearShuntCompensators
WITH LinearShuntCompensators
UNWIND LinearShuntCompensators AS LinearShuntCompensator
WITH LinearShuntCompensator.`rdf:ID` AS `rdf:ID`,
	 [item in LinearShuntCompensator._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:LinearShuntCompensator {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PetersenCoil"] AS PetersenCoils
WITH PetersenCoils
UNWIND PetersenCoils AS PetersenCoil
WITH PetersenCoil.`rdf:ID` AS `rdf:ID`,
	 [item in PetersenCoil._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:PetersenCoil {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "EquivalentInjection"] AS EquivalentInjections
WITH EquivalentInjections
UNWIND EquivalentInjections AS EquivalentInjection
WITH EquivalentInjection.`rdf:ID` AS `rdf:ID`,
	 [item in EquivalentInjection._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:EquivalentInjection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PowerTransformer"] AS PowerTransformers
WITH PowerTransformers
UNWIND PowerTransformers AS PowerTransformer
WITH PowerTransformer.`rdf:ID` AS `rdf:ID`,
	 [item in PowerTransformer._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in PowerTransformer._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:PowerTransformer {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PowerTransformerEnd"] AS PowerTransformerEnds
WITH PowerTransformerEnds
UNWIND PowerTransformerEnds AS PowerTransformerEnd
WITH PowerTransformerEnd.`rdf:ID` AS `rdf:ID`,
	 [item in PowerTransformerEnd._children WHERE item._type = "IdentifiedObject.name"][0] AS name, 
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.endNumber"][0] AS endNumber,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.ratedU"][0] AS ratedU,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.ratedS"][0] AS ratedS,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.r"][0] AS r,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.x"][0] AS x,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.r0"][0] AS r0,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.x0"][0] AS x0,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.b"][0] AS b,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.PowerTransformer"][0] AS PowerTransformer,
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.Terminal"][0] AS Terminal,
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.BaseVoltage"][0] AS BaseVoltage

MERGE (m:PowerTransformerEnd {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.endNumber = endNumber._text,
m.ratedU = ratedU._text,
m.ratedS = ratedS._text,
m.r = r._text,
m.x = x._text,
m.r0 = r0._text,
m.x0 = x0._text,
m.b = b._text,
m.PowerTransformer = substring(PowerTransformer.`rdf:resource`, 1),
m.Terminal = substring(Terminal.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PSRType"] AS PSRTypes
WITH PSRTypes
UNWIND PSRTypes AS PSRType
WITH PSRType.`rdf:ID` AS `rdf:ID`,
	 [item in PSRType._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:PSRType {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "RatioTapChanger"] AS RatioTapChangers
WITH RatioTapChangers
UNWIND RatioTapChangers AS RatioTapChanger
WITH RatioTapChanger.`rdf:ID` AS `rdf:ID`,
	 [item in RatioTapChanger._children WHERE item._type = "IdentifiedObject.name"][0] AS name, 
	 [item in RatioTapChanger._children WHERE item._type = "RatioTapChanger.stepVoltageIncrement"][0] AS stepVoltageIncrement,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.highStep"][0] AS highStep,
	 [item in RatioTapChanger._children WHERE item._type = "RatioTapChanger.tculControlMode"][0] AS tculControlMode,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.lowStep"][0] AS lowStep,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.ltcFlag"][0] AS ltcFlag,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.neutralStep"][0] AS neutralStep,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.neutralU"][0] AS neutralU,
	 [item in RatioTapChanger._children WHERE item._type = "TapChanger.normalStep"][0] AS normalStep,
	 [item in RatioTapChanger._children WHERE item._type = "RatioTapChanger.TransformerEnd"][0] AS TransformerEnd

MERGE (m:RatioTapChanger {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.stepVoltageIncrement = stepVoltageIncrement._text,
m.tculControlMode = tculControlMode._text,
m.highStep = highStep._text,
m.lowStep = lowStep._text,
m.ltcFlag = ltcFlag._text,
m.neutralStep = neutralStep._text,
m.neutralU = neutralU._text,
m.normalStep = normalStep._text,
m.TransformerEnd = substring(TransformerEnd.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "SubGeographicalRegion"] AS SubGeographicalRegions
WITH SubGeographicalRegions
UNWIND SubGeographicalRegions AS SubGeographicalRegion
WITH SubGeographicalRegion.`rdf:ID` AS `rdf:ID`,
	 [item in SubGeographicalRegion._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in SubGeographicalRegion._children WHERE item._type = "IdentifiedObject.description"][0] AS description

MERGE (m:SubGeographicalRegion {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.description = description._text
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Substation"] AS Substations
WITH Substations
UNWIND Substations AS Substation
WITH Substation.`rdf:ID` AS `rdf:ID`,
	 [item in Substation._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Substation._children WHERE item._type = "IdentifiedObject.description"][0] AS description,
	 [item in Substation._children WHERE item._type = "PowerSystemResource.PSRType"][0] AS PSRType,
	 [item in Substation._children WHERE item._type = "Substation.SubGeographicalRegion"][0] AS SubGeographicalRegion

MERGE (m:Substation {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.description = description._text,
m.PSRType = substring(PSRType.`rdf:resource`, 1),
m.SubGeographicalRegion = substring(SubGeographicalRegion.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Terminal"] AS Terminals
WITH Terminals
UNWIND Terminals AS Terminal
WITH Terminal.`rdf:ID` AS `rdf:ID`,
	 [item in Terminal._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Terminal._children WHERE item._type = "ACDCTerminal.sequenceNumber"][0] AS sequenceNumber,
	 [item in Terminal._children WHERE item._type = "Terminal.ConnectivityNode"][0] AS ConnectivityNode,
	 [item in Terminal._children WHERE item._type = "Terminal.ConductingEquipment"][0] AS ConductingEquipment

MERGE (m:Terminal {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.sequenceNumber = sequenceNumber._text,
m.ConnectivityNode = substring(ConnectivityNode.`rdf:resource`, 1),
m.ConductingEquipment = substring(ConductingEquipment.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "VoltageLevel"] AS VoltageLevels
WITH VoltageLevels
UNWIND VoltageLevels AS VoltageLevel
WITH VoltageLevel.`rdf:ID` AS `rdf:ID`,
	 [item in VoltageLevel._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in VoltageLevel._children WHERE item._type = "VoltageLevel.BaseVoltage"][0] AS BaseVoltage,
	 [item in VoltageLevel._children WHERE item._type = "VoltageLevel.Substation"][0] AS Substation

MERGE (m:VoltageLevel {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.Substation = substring(Substation.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "UsagePoint"] AS UsagePoints
WITH UsagePoints
UNWIND UsagePoints AS UsagePoint
WITH UsagePoint.`rdf:ID` AS `rdf:ID`,
	 [item in UsagePoint._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in UsagePoint._children WHERE item._type = "UsagePoint.Equipments"][0] AS Equipments

MERGE (m:UsagePoint {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.Equipments = 	substring(Equipments.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "CurrentLimit"] AS CurrentLimits
WITH CurrentLimits
UNWIND CurrentLimits AS CurrentLimit
WITH CurrentLimit.`rdf:ID` AS `rdf:ID`,
	 [item in CurrentLimit._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in CurrentLimit._children WHERE item._type = "CurrentLimit.value"][0] AS value,
	 [item in CurrentLimit._children WHERE item._type = "OperationalLimit.OperationalLimitSet"][0] AS OperationalLimitSet,
	 [item in CurrentLimit._children WHERE item._type = "OperationalLimit.OperationalLimitType"][0] AS OperationalLimitType

MERGE (m:CurrentLimit {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.value = value._text,
m.OperationalLimitSet = substring(OperationalLimitSet.`rdf:resource`, 1),
m.OperationalLimitType = substring(OperationalLimitType.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "OperationalLimitSet"] AS OperationalLimitSets
WITH OperationalLimitSets
UNWIND OperationalLimitSets AS OperationalLimitSet
WITH OperationalLimitSet.`rdf:ID` AS `rdf:ID`,
	 [item in OperationalLimitSet._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in OperationalLimitSet._children WHERE item._type = "IdentifiedObject.description"][0] AS description,
	 [item in OperationalLimitSet._children WHERE item._type = "OperationalLimitSet.Terminal"][0] AS Terminal

MERGE (m:OperationalLimitSet {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.description = description._text,
m.Terminal = substring(Terminal.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "OperationalLimitType"] AS OperationalLimitTypes
WITH OperationalLimitTypes
UNWIND OperationalLimitTypes AS OperationalLimitType
WITH OperationalLimitType.`rdf:ID` AS `rdf:ID`,
	 [item in OperationalLimitType._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in OperationalLimitType._children WHERE item._type = "OperationalLimitType.acceptableDuration"][0] AS acceptableDuration

MERGE (m:OperationalLimitType {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.acceptableDuration = acceptableDuration._text
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "StationSupply"] AS StationSupplys
WITH StationSupplys
UNWIND StationSupplys AS StationSupply
WITH StationSupply.`rdf:ID` AS `rdf:ID`,
	 [item in StationSupply._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in StationSupply._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in StationSupply._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:StationSupply {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///20210121_DP_CIM_LS_Test1_400V.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Breaker"] AS Breakers
WITH Breakers
UNWIND Breakers AS Breaker
WITH Breaker.`rdf:ID` AS `rdf:ID`,
	 [item in Breaker._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Breaker._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Breaker._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Breaker {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

MATCH (n), (b) WHERE n.PSRType = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.BaseVoltage = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.EquipmentContainer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.PowerTransformer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.Terminal = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.TransformerEnd = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.ConnectivityNode = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.ConductingEquipment = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.Equipments = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.Substation = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.SubGeographicalRegion = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.VoltageLevel = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.OperationalLimitSet = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.OperationalLimitType = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.ConnectivityNodeContainer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);
```

### Only conductivity

```cypher
//Input files: DIGIN10-24-MV1_EQ.xml and/or Nordic44Boundary_24_EQBP.xml

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ACLineSegment"] AS ACLineSegments
WITH ACLineSegments
UNWIND ACLineSegments AS ACLineSegment
WITH ACLineSegment.`rdf:ID` AS `rdf:ID`,
	 [item in ACLineSegment._children WHERE item._type = "PowerSystemResource.PSRType"][0] AS PSRType,
	 [item in ACLineSegment._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in ACLineSegment._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ACLineSegment._children WHERE item._type = "Conductor.length"][0] AS length,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.b0ch"][0] AS b0ch,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.bch"][0] AS bch,
     [item in ACLineSegment._children WHERE item._type = "ACLineSegment.r"][0] AS r,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.r0"][0] AS r0,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.x"][0] AS x,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.x0"][0] AS x0,
	 [item in ACLineSegment._children WHERE item._type = "ACLineSegment.shortCircuitEndTemperature"][0] AS shortCircuitEndTemperature

MERGE (m:ACLineSegment {`rdf:ID`: `rdf:ID`})
SET
m.PSRType = substring(PSRType.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.name = name._text,
m.length = length._text,
m.b0ch = b0ch._text,
m.bch = bch._text,
m.r = r._text,
m.r0 = r0._text,
m.x = x._text,
m.x0 = x0._text,
m.shortCircuitEndTemperature = shortCircuitEndTemperature._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "BusbarSection"] AS BusbarSections
WITH BusbarSections
UNWIND BusbarSections AS BusbarSection
WITH BusbarSection.`rdf:ID` AS `rdf:ID`,
	 [item in BusbarSection._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in BusbarSection._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in BusbarSection._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:BusbarSection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ConformLoad"] AS ConformLoads
WITH ConformLoads
UNWIND ConformLoads AS ConformLoad
WITH ConformLoad.`rdf:ID` AS `rdf:ID`,
	 [item in ConformLoad._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ConformLoad._children WHERE item._type = "ConductingEquipment.BaseVoltage"][0] AS BaseVoltage,
	 [item in ConformLoad._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:ConformLoad {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1),
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "ConnectivityNode"] AS ConnectivityNodes
WITH ConnectivityNodes
UNWIND ConnectivityNodes AS ConnectivityNode
WITH ConnectivityNode.`rdf:ID` AS `rdf:ID`,
	 [item in ConnectivityNode._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in ConnectivityNode._children WHERE item._type = "ConnectivityNode.ConnectivityNodeContainer"][0] AS ConnectivityNodeContainer

MERGE (m:ConnectivityNode {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.ConnectivityNodeContainer = substring(ConnectivityNodeContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Fuse"] AS Fuses
WITH Fuses
UNWIND Fuses AS Fuse
WITH Fuse.`rdf:ID` AS `rdf:ID`,
	 [item in Fuse._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Fuse._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Fuse._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Fuse {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "LoadBreakSwitch"] AS LoadBreakSwitchs
WITH LoadBreakSwitchs
UNWIND LoadBreakSwitchs AS LoadBreakSwitch
WITH LoadBreakSwitch.`rdf:ID` AS `rdf:ID`,
	 [item in LoadBreakSwitch._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in LoadBreakSwitch._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in LoadBreakSwitch._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:LoadBreakSwitch {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Disconnector"] AS Disconnectors
WITH Disconnectors
UNWIND Disconnectors AS Disconnector
WITH Disconnector.`rdf:ID` AS `rdf:ID`,
	 [item in Disconnector._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Disconnector._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Disconnector._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Disconnector {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "SynchronousMachine"] AS SynchronousMachines
WITH SynchronousMachines
UNWIND SynchronousMachines AS SynchronousMachine
WITH SynchronousMachine.`rdf:ID` AS `rdf:ID`,
	 [item in SynchronousMachine._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:SynchronousMachine {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "LinearShuntCompensator"] AS LinearShuntCompensators
WITH LinearShuntCompensators
UNWIND LinearShuntCompensators AS LinearShuntCompensator
WITH LinearShuntCompensator.`rdf:ID` AS `rdf:ID`,
	 [item in LinearShuntCompensator._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:LinearShuntCompensator {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PetersenCoil"] AS PetersenCoils
WITH PetersenCoils
UNWIND PetersenCoils AS PetersenCoil
WITH PetersenCoil.`rdf:ID` AS `rdf:ID`,
	 [item in PetersenCoil._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:PetersenCoil {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "EquivalentInjection"] AS EquivalentInjections
WITH EquivalentInjections
UNWIND EquivalentInjections AS EquivalentInjection
WITH EquivalentInjection.`rdf:ID` AS `rdf:ID`,
	 [item in EquivalentInjection._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:EquivalentInjection {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PowerTransformer"] AS PowerTransformers
WITH PowerTransformers
UNWIND PowerTransformers AS PowerTransformer
WITH PowerTransformer.`rdf:ID` AS `rdf:ID`,
	 [item in PowerTransformer._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in PowerTransformer._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:PowerTransformer {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PowerTransformerEnd"] AS PowerTransformerEnds
WITH PowerTransformerEnds
UNWIND PowerTransformerEnds AS PowerTransformerEnd
WITH PowerTransformerEnd.`rdf:ID` AS `rdf:ID`,
	 [item in PowerTransformerEnd._children WHERE item._type = "IdentifiedObject.name"][0] AS name, 
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.endNumber"][0] AS endNumber,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.ratedU"][0] AS ratedU,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.ratedS"][0] AS ratedS,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.r"][0] AS r,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.x"][0] AS x,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.r0"][0] AS r0,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.x0"][0] AS x0,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.b"][0] AS b,
	 [item in PowerTransformerEnd._children WHERE item._type = "PowerTransformerEnd.PowerTransformer"][0] AS PowerTransformer,
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.Terminal"][0] AS Terminal,
	 [item in PowerTransformerEnd._children WHERE item._type = "TransformerEnd.BaseVoltage"][0] AS BaseVoltage

MERGE (m:PowerTransformerEnd {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.endNumber = endNumber._text,
m.ratedU = ratedU._text,
m.ratedS = ratedS._text,
m.r = r._text,
m.x = x._text,
m.r0 = r0._text,
m.x0 = x0._text,
m.b = b._text,
m.PowerTransformer = substring(PowerTransformer.`rdf:resource`, 1),
m.Terminal = substring(Terminal.`rdf:resource`, 1),
m.BaseVoltage = substring(BaseVoltage.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "PSRType"] AS PSRTypes
WITH PSRTypes
UNWIND PSRTypes AS PSRType
WITH PSRType.`rdf:ID` AS `rdf:ID`,
	 [item in PSRType._children WHERE item._type = "IdentifiedObject.name"][0] AS name

MERGE (m:PSRType {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Terminal"] AS Terminals
WITH Terminals
UNWIND Terminals AS Terminal
WITH Terminal.`rdf:ID` AS `rdf:ID`,
	 [item in Terminal._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Terminal._children WHERE item._type = "ACDCTerminal.sequenceNumber"][0] AS sequenceNumber,
	 [item in Terminal._children WHERE item._type = "Terminal.ConnectivityNode"][0] AS ConnectivityNode,
	 [item in Terminal._children WHERE item._type = "Terminal.ConductingEquipment"][0] AS ConductingEquipment

MERGE (m:Terminal {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.sequenceNumber = sequenceNumber._text,
m.ConnectivityNode = substring(ConnectivityNode.`rdf:resource`, 1),
m.ConductingEquipment = substring(ConductingEquipment.`rdf:resource`, 1)
;

CALL apoc.load.xml("file:///DIGIN10-24-MV1_EQ.xml")
YIELD value
WITH [item in value._children WHERE item._type = "Breaker"] AS Breakers
WITH Breakers
UNWIND Breakers AS Breaker
WITH Breaker.`rdf:ID` AS `rdf:ID`,
	 [item in Breaker._children WHERE item._type = "IdentifiedObject.name"][0] AS name,
	 [item in Breaker._children WHERE item._type = "Switch.normalOpen"][0] AS normalOpen,
	 [item in Breaker._children WHERE item._type = "Equipment.EquipmentContainer"][0] AS EquipmentContainer

MERGE (m:Breaker {`rdf:ID`: `rdf:ID`})
SET
m.name = name._text,
m.normalOpen = normalOpen._text,
m.EquipmentContainer = substring(EquipmentContainer.`rdf:resource`, 1)
;

MATCH (n), (b) WHERE n.PowerTransformer = b.`rdf:ID` MERGE (n)-[r:ref]->(b);

MATCH (n), (b) WHERE n.Terminal = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.ConnectivityNode = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);

MATCH (n), (b) WHERE n.ConductingEquipment = b.`rdf:ID` MERGE (n)-[c:conducting]->(b);
```
