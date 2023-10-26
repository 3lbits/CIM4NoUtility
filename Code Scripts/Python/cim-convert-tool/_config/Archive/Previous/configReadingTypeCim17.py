configReadingTypeCim17 = \
    {
        'cim:ReadingType': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
            },
            'attributes': {
                'skos:exactMatch': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.macroPeriod': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.aggregate': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.measuringPeriod': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.accumulation': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.flowDirection': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.commodity': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.measurementKind': {'rdf:resource': {'type': 'string'}, 'list': False},

                # 'cim:ReadingType.interharmonicNumerator': {'rdf:resource': {'type': 'string'}, 'list': False}, # Not cim
                # 'cim:ReadingType.interharmonicDenominator': {'rdf:resource': {'type': 'string'}, 'list': False}, # Not cim
                # 'cim:ReadingType.argumentNumerator': {'rdf:resource': {'type': 'string'}, 'list': False}, # Not cim
                # 'cim:ReadingType.argumentDenominator': {'rdf:resource': {'type': 'string'}, 'list': False}, # Not cim

                'cim:ReadingType.tou': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.cpp': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.consumptionTier': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.phases': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.multiplier': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.unit': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ReadingType.currency': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }