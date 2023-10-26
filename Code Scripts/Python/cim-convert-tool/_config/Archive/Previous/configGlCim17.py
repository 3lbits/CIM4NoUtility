configGlCim17 = \
    {
        'cim:CoordinateSystem': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:CoordinateSystem.crsUrn': {'type': 'string', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:Location': {
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
                'cim:Location.CoordinateSystem': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Location.PowerSystemResources': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:PositionPoint': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:PositionPoint.sequenceNumber': {'type': 'int', 'list': False},
                'cim:PositionPoint.xPosition': {'type': 'float', 'list': False},
                'cim:PositionPoint.yPosition': {'type': 'float', 'list': False},
                'cim:PositionPoint.zPosition': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:PositionPoint.Location': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }