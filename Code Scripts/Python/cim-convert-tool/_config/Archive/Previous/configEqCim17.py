configEqCim17 = \
    {
        'cim:ACLineSegment': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:Conductor.length': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:ACLineSegment.bch': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Susceptance.value'},
                'cim:ACLineSegment.gch': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Conductance.value'},
                # 'cim:ACLineSegment.r0': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:ACLineSegment.r': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:ACLineSegment.x': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'}
                # 'cim:ACLineSegment.x0': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'}
            },
            'attributes': {
                'cim:PowerSystemResource.AssetDatasheet': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Bay': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:Bay.VoltageLevel': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Breaker': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.normalOpen': {'type': 'bool', 'list': False},
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:Switch.retained': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:BusbarSection': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:ConformLoad': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:EnergyConsumer.pfixed': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EnergyConsumer.pfixedPct': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EnergyConsumer.qfixed': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'},
                'cim:EnergyConsumer.qfixedPct': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:EnergyConsumer.LoadResponse': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConformLoad.LoadGroup': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:ConformLoadGroup': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}

            },
            'attributes': {
                'cim:LoadGroup.SubLoadArea': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:ConnectivityNode': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}

            },
            'attributes': {
                'cim:ConnectivityNode.ConnectivityNodeContainer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:ControlArea': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}

            },
            'attributes': {
                'cim:ControlArea.type': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ControlArea.EnergyArea': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:CurrentLimit': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:CurrentLimit.normalValue': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'}

            },
            'attributes': {
                'cim:OperationalLimit.OperationalLimitSet': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:OperationalLimit.OperationalLimitType': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Disconnector': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.normalOpen': {'type': 'bool', 'list': False},
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:Switch.retained': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:EquivalentInjection': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:EquivalentInjection.maxP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EquivalentInjection.maxQ': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'},
                'cim:EquivalentInjection.minP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EquivalentInjection.minQ': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'},
                'cim:EquivalentInjection.r': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:EquivalentInjection.regulationCapability': {'type': 'bool', 'list': False},
                'cim:EquivalentInjection.x': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Fuse': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.normalOpen': {'type': 'bool', 'list': False},
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:Switch.retained': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:GeneratingUnit': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:GeneratingUnit.highControlLimit': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.initialP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.lowControlLimit': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.maxEconomicP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.maxOperatingP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.minEconomicP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.minOperatingP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.nominalP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.ratedGrossMaxP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:GeneratingUnit.ratedNetMaxP': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Line': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}

            },
            'attributes': {
                'cim:Line.Region': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:LinearShuntCompensator': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:ShuntCompensator.aVRDelay': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Seconds.value'},
                'cim:ShuntCompensator.maximumSections': {'type': 'int', 'list': False},
                'cim:ShuntCompensator.nomU': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'},
                'cim:ShuntCompensator.normalSections': {'type': 'int', 'list': False},
                'cim:LinearShuntCompensator.bPerSection': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Susceptance.value'},
                'cim:LinearShuntCompensator.gPerSection': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Conductance.value'}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:RegulatingCondEq.RegulatingControl': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:LoadArea': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:LoadBreakSwitch': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:Switch.locked': {'type': 'bool', 'list': False},
                'cim:Switch.normalOpen': {'type': 'bool', 'list': False},
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:Switch.retained': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ConductingEquipment.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:LoadResponseCharacteristic': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:LoadResponseCharacteristic.pConstantPower': {'type': 'float', 'list': False},
                'cim:LoadResponseCharacteristic.pConstantCurrent': {'type': 'float', 'list': False},
                'cim:LoadResponseCharacteristic.pConstantImpedance': {'type': 'float', 'list': False},
                'cim:LoadResponseCharacteristic.qConstantPower': {'type': 'float', 'list': False},
                'cim:LoadResponseCharacteristic.qConstantCurrent': {'type': 'float', 'list': False},
                'cim:LoadResponseCharacteristic.qConstantImpedance': {'type': 'float', 'list': False},
                'cim:LoadResponseCharacteristic.exponentModel': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:OperationalLimitSet': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:OperationalLimitSet.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:OperationalLimitType': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:OperationalLimitType.acceptableDuration': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:OperationalLimitType.direction': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:OperationalLimitType.kind': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:PetersenCoil': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:PowerTransformer': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:PowerTransformer.isPartOfGeneratorUnit': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:PowerTransformerEnd': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:TransformerEnd.endNumber': {'type': 'int', 'list': False},
                'cim:TransformerEnd.grounded': {'type': 'bool', 'list': False},
                'cim:PowerTransformerEnd.b': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Susceptance.value'},
                'cim:PowerTransformerEnd.r': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:PowerTransformerEnd.ratedS': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ApparentPower.value'},
                'cim:PowerTransformerEnd.ratedU': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'},
                'cim:PowerTransformerEnd.x': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'}
            },
            'attributes': {
                'cim:PowerTransformerEnd.connectionKind': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:TransformerEnd.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:TransformerEnd.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:PowerTransformerEnd.PowerTransformer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:RatioTapChanger': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:TapChanger.highStep': {'type': 'int', 'list': False},
                'cim:TapChanger.lowStep': {'type': 'int', 'list': False},
                'cim:TapChanger.ltcFlag': {'type': 'bool', 'list': False},
                'cim:TapChanger.neutralStep': {'type': 'int', 'list': False},
                'cim:TapChanger.neutralU': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'},
                'cim:TapChanger.normalStep': {'type': 'int', 'list': False},
                'cim:RatioTapChanger.stepVoltageIncrement': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:PerCent.value'}
            },
            'attributes': {
                'cim:RatioTapChanger.tculControlMode': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:TapChanger.TapChangerControl': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:RatioTapChanger.TransformerEnd': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:RegulatingControl': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:RegulatingControl.mode': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:RegulatingControl.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:StationSupply': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:EnergyConsumer.pfixed': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EnergyConsumer.pfixedPct': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:EnergyConsumer.qfixed': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'},
                'cim:EnergyConsumer.qfixedPct': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'}
            },
            'attributes': {
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SubGeographicalRegion': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:SubGeographicalRegion.Region': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SubLoadArea': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:SubLoadArea.LoadArea': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Substation': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:Substation.Region': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SynchronousMachine': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                # 'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:SynchronousMachine.maxQ': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'},
                'cim:SynchronousMachine.maxU': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'},
                'cim:SynchronousMachine.minQ': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'},
                'cim:SynchronousMachine.minU': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'},
                'cim:SynchronousMachine.qPercent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:PerCent.value'},
                'cim:SynchronousMachine.r': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:SynchronousMachine.referencePriority': {'type': 'int', 'list': False},
                'cim:SynchronousMachine.ratedS': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ApparentPower.value'}
            },
            'attributes': {
                'cim:SynchronousMachine.type': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Equipment.EquipmentContainer': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:RegulatingCondEq.RegulatingControl': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:RotatingMachine.GeneratingUnit': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:TapChangerControl': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:RegulatingControl.mode': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:RegulatingControl.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Terminal': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:ACDCTerminal.sequenceNumber': {'type': 'int', 'list': False}
            },
            'attributes': {
                'cim:Terminal.phases': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Terminal.ConductingEquipment': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Terminal.ConnectivityNode': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:VoltageLevel': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:VoltageLevel.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:VoltageLevel.Substation': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }