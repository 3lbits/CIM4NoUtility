configGeographicalRegionCim17 = \
    {
        'cim:GeographicalRegion': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False}
            },
            'attributes': {

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
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:SubGeographicalRegion.Region': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }