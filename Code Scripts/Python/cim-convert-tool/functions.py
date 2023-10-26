from decimal import Decimal

def xmlPrefixListReplacer(tags, my_namespaces):
    nameSpaceTags = []
    for tag in tags:
        prefix = tag[:tag.find(":")]
        if prefix not in list(my_namespaces.keys()):
            continue
        nameSpaceTags.append(tag.replace(f"{prefix}:", '{' + my_namespaces[prefix] +'}'))
    return nameSpaceTags

def valueDataTypeConverter(value, type):
    if value != None:
        if type == 'bool' and value == 'true':
            return True
        if type == 'bool' and value == 'false':
            return False
        elif type == 'float':
            return float(value)
        elif type == 'int':
            return int(value)
        elif type == 'string':
            return str(value)
        elif type == 'dateTime':
            return str(value)
        elif type == 'decimal':
            return str(value)