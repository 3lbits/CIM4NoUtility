configReadingQualityTypeCim17 = \
    {
        'cim:ReadingQualityType': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:ReadingQualityType.systemId': {'type': 'string', 'list': False},
                'cim:ReadingQualityType.category': {'type': 'string', 'list': False},
                'cim:ReadingQualityType.subCategory': {'type': 'string', 'list': False}
            },
            'attributes': {
                'skos:exactMatch': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }