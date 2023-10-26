configScCim17 = \
    {
        'cim:ACLineSegment': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:ACLineSegment.b0ch': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Susceptance.value'},
                'cim:ACLineSegment.g0ch': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Conductance.value'},
                'cim:ACLineSegment.r0': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:ACLineSegment.shortCircuitEndTemperature': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Temperature.value'},
                'cim:ACLineSegment.x0': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'}
            },
            'attributes': {

            }
        },
        'cim:BusbarSection': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:BusbarSection.ipMax': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'}
            },
            'attributes': {

            }
        },
        'cim:EquivalentInjection': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:EquivalentInjection.r0': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:EquivalentInjection.r': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'},
                'cim:EquivalentInjection.x0': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'},
                'cim:EquivalentInjection.x': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Reactance.value'}
            },
            'attributes': {

            }
        },
        'cim:SynchronousMachine': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:SynchronousMachine.r': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Resistance.value'}
            },
            'attributes': {

            }
        },
        'cim:PetersenCoil': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:PowerTransformer': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:PowerTransformer.isPartOfGeneratorUnit': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:PowerTransformerEnd': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:TransformerEnd.grounded': {'type': 'bool', 'list': False}
            },
            'attributes': {

            }
        }
    }