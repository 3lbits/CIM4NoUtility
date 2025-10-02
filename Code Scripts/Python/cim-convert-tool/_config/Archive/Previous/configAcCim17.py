configAcCim17 = \
    {
        'cim:CableInfo': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:WireInfo.coreRadius': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:WireInfo.coreStrandCount': {'type': 'int', 'list': False},
                'cim:WireInfo.gmr': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:WireInfo.insulated': {'type': 'bool', 'list': False},
                'cim:WireInfo.insulationThickness': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:WireInfo.rAC25': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ResistancePerLength.value'},
                'cim:WireInfo.rAC50': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ResistancePerLength.value'},
                'cim:WireInfo.rAC75': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ResistancePerLength.value'},
                'cim:WireInfo.rDC20': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:ResistancePerLength.value'},
                'cim:WireInfo.radius': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:WireInfo.ratedCurrent': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:CurrentFlow.value'},
                'cim:WireInfo.sizeDescription': {'type': 'string', 'list': False},
                'cim:WireInfo.strandCount': {'type': 'int', 'list': False},
                'cim:CableInfo.diameterOverCore': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:CableInfo.diameterOverInsulation': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:CableInfo.diameterOverJacket': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:CableInfo.diameterOverScreen': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Length.value'},
                'cim:CableInfo.isStrandFill': {'type': 'bool', 'list': False},
                'cim:CableInfo.nominalTemperature': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Temperature.value'},
                'cim:CableInfo.sheathAsNeutral': {'type': 'bool', 'list': False}
            },
            'attributes': {
                'cim:WireInfo.insulationMaterial': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:WireInfo.material': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:CableInfo.constructionKind': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:CableInfo.outerJacketKind': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:CableInfo.shieldMaterial': {'rdf:resource': {'type': 'string'}, 'list': False}

            }
        },
        'cim:PowerTransformerInfo': {
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

            }
        },
        'cim:Manufacturer': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False}
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False}
            },
            'attributes': {
                'cim:Manufacturer.ProductAssetModel': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:ProductAssetModel': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:ProductAssetModel.modelNumber': {'type': 'string', 'list': False},
                'cim:ProductAssetModel.modelVersion': {'type': 'string', 'list': False},
                'cim:ProductAssetModel.drawingNumber': {'type': 'string', 'list': False},
                'cim:ProductAssetModel.instructionMnaual': {'type': 'string', 'list': False},
                'cim:ProductAssetModel.weightTotal': {'type': 'float', 'list': False, 'CIMDatatype': 'cim:Mass.value'}
            },
            'attributes': {
                'cim:ProductAssetModel.AssetModelCatalogueItem': {'rdf:resource': {'type': 'string'}, 'list': False},
                'cim:ProductAssetModel.Manufacturer': {'rdf:resource': {'type': 'string'}, 'list': False}
            }
        },
        'cim:AssetModelCatalogueItem': {
            'mainAttributes': {
                'rdf:ID': {'type': 'string', 'list': False} # @id
            },
            'tags': {
                'cim:IdentifiedObject.mRID': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.aliasName': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.description': {'type': 'string', 'list': False},
                'cim:IdentifiedObject.name': {'type': 'string', 'list': False},
                # 'cim:IdentifiedObject.shortName': {'type': 'string', 'list': False},
                'cim:AssetModelCatalogueItem.unitCost': {'type': 'decimal', 'list': False, 'CIMDatatype': 'cim:Money.value'}
            },
            'attributes': {

            }
        }
    }