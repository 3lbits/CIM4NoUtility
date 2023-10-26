configDlCim17 = \
    {
        'cim:Diagram': {
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
                'cim:Diagram.orientation': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:DiagramObject': {
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
                'cim:DiagramObject.Diagram': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:DiagramObject.DiagramObjectStyle': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:DiagramObject.IdentifiedObject': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:DiagramObjectPoint': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:DiagramObjectPoint.sequenceNumber': {'type': 'int', 'list': False},
                'cim:DiagramObjectPoint.xPosition': {'type': 'float', 'list': False},
                'cim:DiagramObjectPoint.yPosition': {'type': 'float', 'list': False},
                'cim:DiagramObjectPoint.zPosition': {'type': 'float', 'list': False}
            },
            'attributes': {
                'cim:DiagramObjectPoint.DiagramObject': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:DiagramObjectStyle': {
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
        'cim:TextDiagramObject': {
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
                'cim:DiagramObject.Diagram': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:DiagramObject.DiagramObjectStyle': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        }
    }