configAsCim17 = \
    {
        'cim:Asset': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Asset.baselineCondition': {'type': 'string', 'list': False},
                'cim:Asset.baselineLossOfLife': {'type': 'float', 'list': False},
                'cim:Asset.critical': {'type': 'bool', 'list': False},
                'cim:Asset.lotNumber': {'type': 'string', 'list': False},
                'cim:Asset.position': {'type': 'string', 'list': False},
                'cim:Asset.purchasePrice': {'type': 'decimal', 'list': False}, # Actually decimal
                'cim:Asset.serialNumber': {'type': 'string', 'list': False},
                'cim:Asset.type': {'type': 'string', 'list': False},
                'cim:Asset.utcNumber': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:Asset.AssetInfo': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.PowerSystemResources': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.inUseState': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.kind': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.lifecycleState': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Meter': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                'cim:Asset.baselineCondition': {'type': 'string', 'list': False},
                'cim:Asset.baselineLossOfLife': {'type': 'float', 'list': False},
                'cim:Asset.critical': {'type': 'bool', 'list': False},
                'cim:Asset.lotNumber': {'type': 'string', 'list': False},
                'cim:Asset.position': {'type': 'string', 'list': False},
                'cim:Asset.purchasePrice': {'type': 'decimal', 'list': False}, # Actually decimal
                'cim:Asset.serialNumber': {'type': 'string', 'list': False},
                'cim:Asset.type': {'type': 'string', 'list': False},
                'cim:Asset.utcNumber': {'type': 'string', 'list': False},
                'cim:EndDevice.amrSystem': {'type': 'string', 'list': False},
                'cim:EndDevice.installCode': {'type': 'string', 'list': False},
                'cim:EndDevice.isPan': {'type': 'bool', 'list': False},
                'cim:EndDevice.isSmartInverter': {'type': 'bool', 'list': False},
                'cim:EndDevice.isVirtual': {'type': 'bool', 'list': False},
                'cim:EndDevice.timeZoneOffset': {'type': 'float', 'list': False}, # min
                'cim:Meter.connectionCategory': {'type': 'string', 'list': False},
                'cim:Meter.formNumber': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:Asset.AssetInfo': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.PowerSystemResources': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.inUseState': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.kind': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:Asset.lifecycleState': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }