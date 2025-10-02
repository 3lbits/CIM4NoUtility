configOpCim17 = \
    {
        'cim:Analog': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:Measurement.measurementType': {'type': 'string', 'list': False},
                'cim:Analog.maxValue': {'type': 'float', 'list': False},
                'cim:Analog.minValue': {'type': 'float', 'list': False},
                'cim:Analog.normalValue': {'type': 'float', 'list': False},
                'cim:Analog.positiveFlowIn': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:Measurement.phases': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.unitMultiplier': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.unitSymbol': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.Asset': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.PowerSystemResources': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:AnalogValue': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:MeasurementValue.sensorAccuracy': {'type': 'float', 'list': False},
                'cim:MeasurementValue.timeStamp': {'type': 'dateTime', 'list': False},
                'cim:AnalogValue.value': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:AnalogValue.Analog': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Discrete': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:Measurement.measurementType': {'type': 'string', 'list': False},
                'cim:Discrete.maxValue': {'type': 'float', 'list': False},
                'cim:Discrete.minValue': {'type': 'float', 'list': False},
                'cim:Discrete.normalValue': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:Measurement.phases': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.unitMultiplier': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.unitSymbol': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.Asset': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.PowerSystemResource': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Measurement.ACDCTerminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:DiscreteValue': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:MeasurementValue.sensorAccuracy': {'type': 'float', 'list': False},
                'cim:MeasurementValue.timeStamp': {'type': 'dateTime', 'list': False},
                'cim:DiscreteValue.value': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:MeasurementValue.MeasurementValueSource': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:DiscreteValue.Discrete': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:CurrentTransformer': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:CurrentTransformer.accuracyClass': {'type': 'string', 'list': False},
                'cim:CurrentTransformer.accuracyLimit': {'type': 'float', 'list': False},
                'cim:CurrentTransformer.coreBurden': {'type': 'float', 'list': False},
                'cim:CurrentTransformer.ctClass': {'type': 'string', 'list': False},
                'cim:CurrentTransformer.usage': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:AuxiliaryEquipment.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:PotentialTransformer': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:Equipment.aggregate': {'type': 'bool', 'list': False},
                'cim:Equipment.networkAnalysisEnabled': {'type': 'bool', 'list': False},
                'cim:Equipment.normallyInService': {'type': 'bool', 'list': False},
                'cim:PotentialTransformer.accuracyClass': {'type': 'string', 'list': False},
                'cim:PotentialTransformer.nominalRatio': {'type': 'float', 'list': False},
                'cim:PotentialTransformer.ptClass': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:PotentialTransformer.type': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:AuxiliaryEquipment.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:CommunicationLink': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:CommunicationLink.RemoteUnits': {'rdf:resource': {'type': 'string'}, 'list': True}
            }
        },
        'cim:RemoteSource': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:RemoteSource.deadband': {'type': 'float', 'list': False},
                'cim:RemoteSource.scanInterval': {'type': 'float', 'list': False},
                'cim:RemoteSource.sensorMaximum': {'type': 'float', 'list': False},
                'cim:RemoteSource.sensorMinimum': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:RemotePoint.RemoteUnit': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:RemoteUnit': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:RemoteUnit.remoteUnitType': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }