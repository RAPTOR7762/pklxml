from lxml import etree

def load(file_path):
    tree = etree.parse(file_path)
    return _deserialize(tree.getroot())

def _deserialize(element):
    tag = element.tag
    if tag == 'variable':
        value_type = element.attrib['type']
        return _cast(element.text, value_type)
    elif tag == 'list':
        return [_cast(item.text, item.attrib['type']) for item in element.findall('item')]
    elif tag == 'tuple':
        return tuple(_cast(item.text, item.attrib['type']) for item in element.findall('item'))
    elif tag == 'dict':
        result = {}
        for item in element.findall('item'):
            key_el = item.find('key')
            val_el = item.find('value')
            key = _cast(key_el.text, key_el.attrib['type'])
            if len(val_el):  # nested structure
                val = _deserialize(val_el)
            else:
                val = _cast(val_el.text, val_el.attrib['type'])
            result[key] = val
        return result
    else:
        return None

def _cast(value, value_type):
    if value_type == 'int': return int(value)
    if value_type == 'float': return float(value)
    if value_type == 'str': return value
    if value_type == 'bool': return value.lower() == 'true'
    return value  # fallback
