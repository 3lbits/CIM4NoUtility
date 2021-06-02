# Digin10

# EQ
ACLineSegment
- <cim:IdentifiedObject.aliasName></cim:IdentifiedObject.aliasName> <!--Optional-->
- <cim:Equipment.networkAnalysisEnabled>true</cim:Equipment.networkAnalysisEnabled> <!--Optional, If not used then true-->
- <cim:Equipment.normallyInService>true</cim:Equipment.normallyInService> <!--Optional, If not used then true-->
- <cim:Conductor.length>0.03125</cim:Conductor.length> <!--Make mandatory-->
- <cim:ACLineSegment.b0ch>0</cim:ACLineSegment.b0ch> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.bch>0</cim:ACLineSegment.bch> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.g0ch>0</cim:ACLineSegment.g0ch> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.gch>0</cim:ACLineSegment.gch> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.r0>0</cim:ACLineSegment.r0> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.shortCircuitEndTemperature>0</cim:ACLineSegment.shortCircuitEndTemperature> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.x0>0</cim:ACLineSegment.x0> <!--Mandatory IF http://entsoe.eu/CIM/EquipmentShortCircuit/3/1-->
- <cim:ACLineSegment.x>0.0000031250001484295353</cim:ACLineSegment.x>
- <cim:Equipment.AdditionalEquipmentContainer rdf:resource="#_fb2959cd-e32f-4109-add8-8c9a2e8ff11d"/> <!--Feeder-Operation-->
- Bay
  - Fjernes
    - <cim:Bay.bayEnergyMeasFlag>false</cim:Bay.bayEnergyMeasFlag>
    - <cim:Bay.bayPowerMeasFlag>false</cim:Bay.bayPowerMeasFlag>
  - Backlog
    - <cim:Bay.breakerConfiguration></cim:Bay.breakerConfiguration>
    - <cim:Bay.busBarConfiguration></cim:Bay.busBarConfiguration>
- Switch
  - Optional
    - <cim:Switch.locked></cim:Switch.locked> - optional SSH CGMES 3.0
    - <cim:ProtectedSwitch.breakingCapacity></cim:ProtectedSwitch.breakingCapacity>
    - <cim:Breaker.inTransitTime></cim:Breaker.inTransitTime>
  - SSH
    - <cim:Switch.open></cim:Switch.open>
  - Fjernes
    - <cim:Switch.switchOnCount></cim:Switch.switchOnCount>
    - <cim:Switch.switchOnDate></cim:Switch.switchOnDate>
    
- Transferred to Boundry
  - <cim:ConnectivityNode rdf:ID="_df2ee556-3539-4772-aa10-052af1fab06f">
        <cim:IdentifiedObject.description>400 Volt Telemarkstien 2 Connectivity Node 2 BoundryPoint</cim:IdentifiedObject.description>
        <cim:IdentifiedObject.name>04 Telemarkstien 2 CN2 BP</cim:IdentifiedObject.name>
        <cim:IdentifiedObject.aliasName></cim:IdentifiedObject.aliasName>
        <cim:ConnectivityNode.ConnectivityNodeContainer rdf:resource="#_6a779c50-8ec1-48e6-8c9d-b36c379b08f4"/>
    </cim:ConnectivityNode>

ConnectivityNode
- Fjerner aliasName

CurrentLimit
- Fjerner description
- Fjerner aliasName

LV EQ
- Missing TATL
- Missing ExternalNetworkInjection
- Missing EquivalentInjection

Remvoed:
        <cim:VoltageLevel.highVoltageLimit></cim:VoltageLevel.highVoltageLimit>
        <cim:VoltageLevel.lowVoltageLimit></cim:VoltageLevel.lowVoltageLimit>

## Feeder

![Feeder](/Feeder.drawio.png)

## MV

![MV](/DIGIN10-24-MV1_EQ.drawio.png)

## LV

![LV](/DIGIN10-24-LV1_EQ.drawio.png)