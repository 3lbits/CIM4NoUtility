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
                'cim:Conductor.length': {'type': 'float', 'list': False},
                'cim:ACLineSegment.bch': {'type': 'float', 'list': False},
                'cim:ACLineSegment.gch': {'type': 'float', 'list': False},
                # 'cim:ACLineSegment.r0': {'type': 'float', 'list': False},
                'cim:ACLineSegment.r': {'type': 'float', 'list': False},
                'cim:ACLineSegment.x': {'type': 'float', 'list': False}
                # 'cim:ACLineSegment.x0': {'type': 'float', 'list': False}
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
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False},
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
                'cim:EnergyConsumer.pfixed': {'type': 'float', 'list': False},
                'cim:EnergyConsumer.pfixedPct': {'type': 'float', 'list': False},
                'cim:EnergyConsumer.qfixed': {'type': 'float', 'list': False},
                'cim:EnergyConsumer.qfixedPct': {'type': 'float', 'list': False}
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
                'cim:CurrentLimit.normalValue': {'type': 'float', 'list': False}

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
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False},
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
                'cim:EquivalentInjection.maxP': {'type': 'float', 'list': False},
                'cim:EquivalentInjection.maxQ': {'type': 'float', 'list': False},
                'cim:EquivalentInjection.minP': {'type': 'float', 'list': False},
                'cim:EquivalentInjection.minQ': {'type': 'float', 'list': False},
                'cim:EquivalentInjection.r': {'type': 'float', 'list': False},
                'cim:EquivalentInjection.regulationCapability': {'type': 'bool', 'list': False},
                'cim:EquivalentInjection.x': {'type': 'float', 'list': False}
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
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False},
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
                'cim:GeneratingUnit.highControlLimit': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.initialP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.lowControlLimit': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.maxEconomicP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.maxOperatingP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.minEconomicP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.minOperatingP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.nominalP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.ratedGrossMaxP': {'type': 'float', 'list': False},
                'cim:GeneratingUnit.ratedNetMaxP': {'type': 'float', 'list': False}
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
                'cim:ShuntCompensator.aVRDelay': {'type': 'float', 'list': False},
                'cim:ShuntCompensator.maximumSections': {'type': 'int', 'list': False},
                'cim:ShuntCompensator.nomU': {'type': 'float', 'list': False},
                'cim:ShuntCompensator.normalSections': {'type': 'int', 'list': False},
                'cim:LinearShuntCompensator.bPerSection': {'type': 'float', 'list': False},
                'cim:LinearShuntCompensator.gPerSection': {'type': 'float', 'list': False}
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
                'cim:Switch.ratedCurrent': {'type': 'float', 'list': False},
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
                'eu:OperationalLimitType.kind': {'rdf:resource': {'type': 'string'}, 'list': False}
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
                'cim:PowerTransformerEnd.b': {'type': 'float', 'list': False},
                'cim:PowerTransformerEnd.r': {'type': 'float', 'list': False},
                'cim:PowerTransformerEnd.ratedS': {'type': 'float', 'list': False},
                'cim:PowerTransformerEnd.ratedU': {'type': 'float', 'list': False},
                'cim:PowerTransformerEnd.x': {'type': 'float', 'list': False}
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
                'cim:TapChanger.neutralU': {'type': 'float', 'list': False},
                'cim:TapChanger.normalStep': {'type': 'int', 'list': False},
                'cim:RatioTapChanger.stepVoltageIncrement': {'type': 'float', 'list': False}
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
                'cim:EnergyConsumer.pfixed': {'type': 'float', 'list': False},
                'cim:EnergyConsumer.pfixedPct': {'type': 'float', 'list': False},
                'cim:EnergyConsumer.qfixed': {'type': 'float', 'list': False},
                'cim:EnergyConsumer.qfixedPct': {'type': 'float', 'list': False}
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
                'cim:SynchronousMachine.maxQ': {'type': 'float', 'list': False},
                'cim:SynchronousMachine.maxU': {'type': 'float', 'list': False},
                'cim:SynchronousMachine.minQ': {'type': 'float', 'list': False},
                'cim:SynchronousMachine.minU': {'type': 'float', 'list': False},
                'cim:SynchronousMachine.qPercent': {'type': 'float', 'list': False},
                'cim:SynchronousMachine.r': {'type': 'float', 'list': False},
                'cim:SynchronousMachine.referencePriority': {'type': 'int', 'list': False},
                'cim:SynchronousMachine.ratedS': {'type': 'float', 'list': False}
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