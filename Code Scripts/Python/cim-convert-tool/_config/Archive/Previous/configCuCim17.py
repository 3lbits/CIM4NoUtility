configCuCim17 = \
    {
        'cim:UsagePoint': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:UsagePoint.chekBilling': {'type': 'bool', 'list': False},
                'cim:UsagePoint.connectionCategory': {'type': 'string', 'list': False},
                'cim:UsagePoint.disconnectionMethod': {'type': 'string', 'list': False},
                'cim:UsagePoint.estimatedLoad': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:UsagePoint.grounded': {'type': 'bool', 'list': False},
                'cim:UsagePoint.isSdq': {'type': 'bool', 'list': False},
                'cim:UsagePoint.isVirtual': {'type': 'bool', 'list': False},
                'cim:UsagePoint.minimalUsageExpected': {'type': 'bool', 'list': False},
                'cim:UsagePoint.nominalServiceVoltage': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Voltage.value'},
                'cim:UsagePoint.outageRegion': {'type': 'string', 'list': False},
                'cim:UsagePoint.phaseCount': {'type': 'int', 'list': False},
                'cim:UsagePoint.ratedCurrent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:UsagePoint.ratedPower': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ActivePower.value'},
                'cim:UsagePoint.readCycle': {'type': 'string', 'list': False},
                'cim:UsagePoint.readRoute': {'type': 'string', 'list': False},
                'cim:UsagePoint.serviceDeliveryRemark': {'type': 'string', 'list': False},
                'cim:UsagePoint.servicePriority': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:UsagePoint.amiBillingReady': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:UsagePoint.connectionState': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:UsagePoint.phaseCode': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:UsagePoint.Equipments': {'rdf:resource': {'type': 'string'}, 'list': True}
            }
        }
    }