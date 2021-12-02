# measurementType naming conventions 

## 61970-301:2020
The table below is taken from 61970-301:2020 Table 6 - measurmentType naming conventions.

measurementType        | 61850 Name | description|
| -------------|-|:-------------|
| Current | Amp | Current (rms) of a non-three phase circuit    | 
|ThreePhaseCurrent|	AvAmps	|Total current (rms) in a three phase circuit|
|PhaseCurrent	|A|	Measured phase current.|
|Frequency	|Hz	|Frequency|
|PowerFactor	|PwrFact|	Power factor not allocated to a phase|
|ThreePhasePowerFactor	|TotPF|	Average power factor in a three phase circuit|
|ThreePhaseApparentPower	|TotVA|	Total apparent power in a three phase circuit|
|ThreePhaseReactivePower	|TotVAr|	Total reactive power in a three phase circuit|
|ThreePhaseActivePower	|TotW|	Total real power in a three phase circuit.|
|ApparentPower	|VolAmp|	Apparent power in a non-three phase circuit|
|ReactivePower	|VolAmpr|	Reactive power in a non-three phase circuit|
|Voltage	|Vol|	Voltage (rms) not allocated to a phase|
|ActivePower	|Watt|	Real power in a non-three phase circuit|
|Pressure	|Pres|	Pressure|
|Temperature	|Tmp|	Temperature|
|Angle	|Ang|	Angle between voltage and current|
|ApparentEnergy	|TotVAh|	Apparent energy|
|ReactiveEnergy	|TotVArh|	Reactive energy|
|ActiveEnergy	|TotWh|	Real energy|
|Automatic	|Auto|	Automatic operation (not manual)|
|LocalOperation	|Loc|	Local operation (not remote)|
|SwitchPosition	|Pos|	Switch position (2bits= intermediate,open,closed,ignore)|
|TapPosition	|TapPos|	Tap position of power transformer or phaseshifter|
|Operation Count	|OperCnt|	Operation count – typically for switches|
|LineToNeutralVoltage||		Line to neutral voltage.|
|LineToGroundVoltage	||	Line to ground voltage.|
|Specialization	||	Used when a specialization of the Analog class defines the type of measurement rather than the Measurement.measurementType attribute.|

## Statnett Extenstions/usage
The table below is describing Statnett extenstion and usage of measurmentType.

measurmentType    |phase [0..1] |   unitMultiplier |   unitSymbol|
| -------------|-|-|:-------------|
PhaseVoltage|PhaseCode.A/B/C|UnitMultiplier.k|UnitSymbol.V|
Frequency||UnitMultiplier.none|UnitSymbol.Hz
Temperature||UnitMultiplier.none|UnitSymbol.degC
governorSpeedChangeDroop||UnitMultiplier.none|UnitSymbol.none
StrokeLimiter||UnitMultiplier.M|UnitSymbol.W
HydrogenConcentration||UnitMultiplier.none|UnitSymbol.none
OxygenConcentration||UnitMultiplier.none|UnitSymbol.none
NitrogenConcentration||UnitMultiplier.none|UnitSymbol.none
CarbonMonozideConcentration||UnitMultiplier.none|UnitSymbol.none
CarbonDioxideConcentration||UnitMultiplier.none|UnitSymbol.none
MethaneConcentration||UnitMultiplier.none|UnitSymbol.none
AcetyleneConcentration||UnitMultiplier.none|UnitSymbol.none
EthyleneConcentration||UnitMultiplier.none|UnitSymbol.none
EthaneConcentration||UnitMultiplier.none|UnitSymbol.none
OilTemperature||UnitMultiplier.none|UnitSymbol.degC
MoistoureConcentration||UnitMultiplier.none|UnitSymbol.none
AciditiryConcentration||UnitMultiplier.none|UnitSymbol.none
Pressure||UnitMultiplier.k|UnitSymbol.Pa
WindingTemperature||UnitMultiplier.none|UnitSymbol.degC
AmbientTemperature||UnitMultiplier.none|UnitSymbol.degC
LightningIndication||UnitMultiplier.none|UnitSymbol.none
CommunicationIndication||UnitMultiplier.none|UnitSymbol.none
BreakerIndication||UnitMultiplier.none|UnitSymbol.none
AlarmIndication||UnitMultiplier.none|UnitSymbol.none
WarningIndication||UnitMultiplier.none|UnitSymbol.none
ErrorIndication||UnitMultiplier.none|UnitSymbol.none
ControlIndication||UnitMultiplier.none|UnitSymbol.none
Indication||UnitMultiplier.none|UnitSymbol.none
