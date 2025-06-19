from lxml import etree
import os, importlib

# Whitelist of safe modules and classes
ALLOWED_CLASSES = {
    "examples.examples_class": ["Person"],  # Extend as needed
}
MAX_DEPTH = 50  # or some other reasonable number

# Custom XMLParser that blocks <!DOCTYPE>
class NoDoctypeParser(etree.XMLParser):
    def __init__(self, **kwargs):
        super().__init__(
            resolve_entities=False,
            no_network=True,
            dtd_validation=False,
            load_dtd=False,
            huge_tree=False,
            **kwargs
        )

    def feed(self, data):
        if b"<!DOCTYPE" in data:
            raise ValueError("DOCTYPE is not allowed in PKLXML.")
        super().feed(data)

def secureParser():
    return NoDoctypeParser()

def load(file_path):
    parser = secureParser()
    tree = etree.parse(file_path, parser)
    
    if validate:
        # Locate the XSD file relative to this script
        xsd_path = os.path.join(os.path.dirname(__file__), "schema", "pklxml.xsd")
        with open(xsd_path, 'rb') as f:
            schema_doc = etree.parse(f)
            
        schema = etree.XMLSchema(schema_doc)
        
        if not schema.validate(tree):
            raise ValueError("XSD validation failed:\n" + str(schema.error_log))

    return _deserialize(tree.getroot())

def _deserialize(element, depth=0):
    if depth > MAX_DEPTH:
        raise ValueError("Maximum deserialization depth exceeded.")
        
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
            if len(val_el):
                val = _deserialize(val_el)
            else:
                val = _cast(val_el.text, val_el.attrib['type'])
            result[key] = val
        return result

    elif tag == 'class':
        module = element.attrib['module']
        class_name = element.attrib['name']
        cls = _import_class_secure(module, class_name)
        obj = cls.__new__(cls)
        for attr in element.findall('attribute'):
            attr_name = attr.attrib['name']
            if len(attr):
                attr_value = _deserialize(attr)
            else:
                attr_value = _cast(attr.text, attr.attrib['type'])
            setattr(obj, attr_name, attr_value)
        return obj

    else:
        raise ValueError(f"Unknown tag: <{element.tag}>")

def _import_class_secure(module_name, class_name):
    allowed = ALLOWED_CLASSES.get(module_name, [])
    if class_name not in allowed:
        print(f"[SECURITY] Blocked class import: {module_name}.{class_name}")
        raise ImportError(f"Import of {class_name} from {module_name} is not allowed.")
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def _cast(value, value_type):
    if value is None:
        return None
    try:
        if value_type == 'int':
            return int(value)
        if value_type == 'float':
            return float(value)
        if value_type == 'str':
            return value
        if value_type == 'bool':
            return value.lower() == 'true'
    except Exception as e:
        raise ValueError(f"Failed to cast value '{value}' as '{value_type}': {e}")
    raise ValueError(f"Unsupported value type: '{value_type}'")
