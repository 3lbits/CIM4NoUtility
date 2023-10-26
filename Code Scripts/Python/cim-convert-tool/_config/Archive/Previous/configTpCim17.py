configTpCim17 = \
    {
        'cim:ConnectivityNode': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {

            },
            'attributes': {
                'cim:ConnectivityNode.TopologicalNode': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:Terminal': {
            'mainAttributes': {
                'rdf:about': {'type': 'string', 'list': False} # @id
            },
            'tags': {

            },
            'attributes': {
                'cim:Terminal.TopologicalNode': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:TopologicalNode': {
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
                'cim:TopologicalNode.BaseVoltage': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:TopologicalNode.ConnectivityNodeContainer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }