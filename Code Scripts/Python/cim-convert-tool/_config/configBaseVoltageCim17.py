configBaseVoltageCim17 = \
    {
        'cim:BasePower': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:BasePower.basePower': {'type': 'float', 'list': False}
            },
            'attributes': {

            }
        },
        'cim:BaseVoltage': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:BaseVoltage.nominalVoltage': {'type': 'float', 'list': False}
            },
            'attributes': {

            }
        }
    }