configSvCim17 = \
    {
        'cim:SvPowerFlow': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:SvPowerFlow.p': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:SvPowerFlow.q': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ReactivePower.value'}
            },
            'attributes': {
                'cim:SvPowerFlow.Terminal': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SvShuntCompensatorSections': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:SvShuntCompensatorSections.sections': {'type': 'float', 'list': False}

            },
            'attributes': {
                'cim:SvShuntCompensatorSections.ShuntCompensator': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SvStatus': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:SvStatus.inService': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:SvStatus.ConductingEquipment': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SvSwitch': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:SvSwitch.open': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:SvSwitch.Switch': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SvTapStep': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:SvTapStep.position': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:SvTapStep.TapChanger': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:SvVoltage': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:SvVoltage.angle': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:AngleDegrees.value'},
                'cim:SvVoltage.v': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'}
            },
            'attributes': {
                'cim:SvVoltage.TopologicalNode': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:TopologicalIsland': {
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
                'cim:TopologicalIsland.AngleRefTopologicalNode': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:TopologicalIsland.TopologicalNodes': {'rdf:resource': {'type': 'string'}, 'list': True}
            }
        }
    }