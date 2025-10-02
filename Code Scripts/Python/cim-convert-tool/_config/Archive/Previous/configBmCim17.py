configBmCim17 = \
    {
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
        'eu:BoundaryPoint': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.isDirectCurrent': {'type': 'boolean', 'list': False},
                'eu:BoundaryPoint.fromEndIsoCode': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.fromEndName': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.fromEndNameTso': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.toEndIsoCode': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.toEndName': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.toEndNameTso': {'type': 'string', 'list': False},
                'eu:BoundaryPoint.isExcludedFromAreaInterchange': {'type': 'boolean', 'list': False}
            },
            'attributes': {
                'eu:BoundaryPoint.ConnectivityNode': {'rdf:resource': {'type': 'string'}, 'list': False}
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