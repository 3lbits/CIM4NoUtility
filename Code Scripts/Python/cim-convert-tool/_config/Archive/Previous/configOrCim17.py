configOrCim17 = \
    {
        'cim:Name': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'nc:Name.mRID': {'type': 'string', 'list': False},
                'cim:Name.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:Name.IdentifiedObject': {'rdf:resource': {'type': 'string'}, 'list': False},
                'nc:Name.NameType': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:NameType': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'nc:NameType.mRID': {'type': 'string', 'list': False},
                'cim:NameType.description': {'type': 'string', 'list': False},
                'cim:NameType.name': {'type': 'string', 'list': False}
            },
            'attributes': {
                'nc:NameType.NameTypeAuthority': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:NameTypeAuthority': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'nc:NameTypeAuthority.mRID': {'type': 'string', 'list': False},
                'cim:NameTypeAuthority.description': {'type': 'string', 'list': False},
                'cim:NameTypeAuthority.name': {'type': 'string', 'list': False}
            },
            'attributes': {

            }
        }
    }