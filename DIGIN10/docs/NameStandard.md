# Standards used for naming

In the Digin model the following standards are used for cim:IdentifiedObject.name and cim:IdentifiedObject.Description.

Name of an instance must be unique.
For each class there is an example of how the a name and description are composed.
General rule:
- Name string shall be in capital letters

## Classes

### cim:ACLineSegment - ACLS

voltage | component("service-name") | component class | sequence number

| Name                       | Description                             |
| -------------------------- | :-------------------------------------- |
| 132 ARENDAL-FROLAND ACLS 1 | 132kV Arendal-Froland 1 ACLineSegment 1 |
| 22 ENGENE-T1 ACLS 1 1      | 22kV Engene Transformer 1 Cable 1       |
| 04 TELEMA 2 ACLS 3         | 400V Telemarkstien 2 ACLineSegment 3    |
| 023 ZT1-EFC ACLS 1         | 230V ZT1-EFC ACLineSegment 1            |

### cim:Bay

| Name           | Description                          |
| -------------- | :----------------------------------- |
| FROLAND 132EN1 | Froland 132kV Engene 1 Bay           |
| ENGENE 22T1    | Engene 22kV Transformer 1 Bay        |
| NEDENES 04LC1  | Nedenes 400V Low Voltage Cable 1 Bay |
| ENGENE 023 ZT1 | Engene 230V Netral Transformer 1     |
| 04 TELEMA 2 Ba1| 400 Volt Telemarkstien 2 Bay 1       |

### cim:Breaker

| Name                   | Description                        |
| ---------------------- | :--------------------------------- |
| FROLAND 132EN1         | Froland 132kV Engene 1 Bay         |
| ENGENE 22 T1E          | Engene 22kV T1 Breaker             |
| 04 TELEMA 2 Br1 | 400 Volt Telemarkstien 2 Breaker 1 |

### cim:BusbarSection

| Name                   | Description                               |
| ---------------------- | :---------------------------------------- |
| FROLAND 132A           | Froland 132kV A Busbar Section            |
| ENGENE 22A             | Engene 22kV A Busbar Section 1            |
| NEDENES 04A            | Nedenes 400V A Busbar Section 1           |
| 04 TELEMA 2 BS1        | 400 Volt Telemarkstien 2 Busbar Section 1 |

### cim:ConnectivityNode

| Name                   | Description                               |
| ---------------------- | :---------------------------------------- |
| ARENDAL CN 007         |                                           |
| 04 TELEMA 2 CN1        | 400 Volt Telemarkstien 2 Connectivity Node 1|

### cim:Disconnector

| Name                 | Description                           |
| -------------------- | :------------------------------------ |
| FROLAND 132 EN1 AD_S | Froland 132kV Engene 1 A Disconnector |
| ENGENE 22 NE1 AD_S   | Engene 22kV Nedenes 1 A Disconnector  |

### cim:Fuse

| Name                    | Description                         |
| ----------------------- | :---------------------------------- |
| NEDENES 22 TELEMA 2 FU1 | Nedenes 22kV Telemarkstien 2 Fuse 1 |

### cim:GeneratingUnit

| Name                    | Description                          |
| ----------------------- | :----------------------------------- |
| ARENDAL 420 G1          | Arendal 420kV Transmission Equivalent|

### cim:Line

| Name                  | Description              |
| --------------------- | :----------------------- |
| LC 132ARENDAL-FROLAND | Line 132 ARENDAL-FROLAND |

### cim:LinearShuntCompensator - SC

| Name          | Description                     |
| ------------- | :------------------------------ |
| ENGENE 22 SC1 | Engene 22kV A Shunt Compensator |

### cim:LoadBreakSwitch

| Name               | Description                             |
| ------------------ | :-------------------------------------- |
| NEDENES 22 E1 LB_S | Nedenes 22kV Engene 1 Load Break Switch |

### cim:PetersenCoil

| Name              | Description                   |
| ----------------- | :---------------------------- |
| ARENDAL 132 T1 PC | Arendal 132kV T1 PetersenCoil |

### cim:PowerTransformer

| Name       | Description                             |
| ---------- | :-------------------------------------- |
| ARENDAL T1 | Arendal 420kV / 132kV Transformer 1     |
| ENGENE T1  | Engene 132kV / 22kV Transformer 1       |
| NEDENES T1 | Nedenes 22kV / 400V Power Transformer 1 |

### cim:PowerTransformerEnd

| Name             | Description                        |
| ---------------- | :--------------------------------- |
| ARENDAL T1 420 P | Arendal T1 420kV Primary Winding   |
| ARENDAL T1 132 S | Arendal T1 132kV Secondary Winding |
| ENGENE ZT1 22 P  | Engene ZT1 22kV Primary Winding    |

### cim:RatioTapChanger

| Name             | Description                        |
| ---------------- | :--------------------------------- |
| ARENDAL T1 420 P | Arendal T1 420kV Primary Winding   |
| ARENDAL T1 132 S | Arendal T1 132kV Secondary Winding |
|                  |                                    |

### cim:RegulatingControl

| Name             | Description                                        |
| ---------------- | :------------------------------------------------- |
| ENGENE 22 SC1 RC | Engene 22kV Shunt Compensator Regulating Control 1 |

### cim:Substation

| Name     | Description                 |
| -------- | :-------------------------- |
| ENGENE   | Engene Substation           |
| FROLAND  | Froland Coupling Substation |
| T_ENGENE | Engene T-junction           |
| 04 TELEMA 2 CB4| 400 Volt Telemarkstien 2 Cable Box 4|

### cim:TapChangerControl

| Name    | Description       |
| ------- | :---------------- |
| ARENDAL |                   |
| ENGENE  | Engene Substation |

### cim:Terminal

| Name                     | Description      |
| ------------------------ | :--------------- |
| T1 132ARENDAL-FROLAND1   | Arendal Side     |
| T1 132 ARENDAL-T1 ACLS 1 | Transformer Side |
| T1 22 ENGENE-T1 ACLS 1 1 | Engene Side      |
| 04 TELEMA 2 T1 | 400 Volt Telemarkstien 2 Terminal 1|

### cim:UsagePoint
| Name                     | Description      |
| ------------------------ | :--------------- |
| 04 TELEMA 2 UP7 | 400 Volt Telemarkstien 2 UsagePoint 7|
