from lxml import etree

def dump(obj, file_path):
    root = etree.Element("pysxml")
    _serialize(obj, root)
    tree = etree.ElementTree(root)
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding='utf-8')

def _serialize(obj, parent):
    if isinstance(obj, dict):
        dict_el = etree.SubElement(parent, "dict")
        for k, v in obj.items():
            item = etree.SubElement(dict_el, "item")
            key = etree.SubElement(item, "key", type=type(k).__name__)
            key.text = str(k)
            value = etree.SubElement(item, "value", type=type(v).__name__)
            _serialize(v, value) if isinstance(v, (dict, list, tuple)) else value.__setattr__('text', str(v))
    elif isinstance(obj, list):
        list_el = etree.SubElement(parent, "list")
        for v in obj:
            item = etree.SubElement(list_el, "item", type=type(v).__name__)
            item.text = str(v)
    elif isinstance(obj, tuple):
        tuple_el = etree.SubElement(parent, "tuple")
        for v in obj:
            item = etree.SubElement(tuple_el, "item", type=type(v).__name__)
            item.text = str(v)
    else:
        etree.SubElement(parent, "variable", name="value", type=type(obj).__name__).text = str(obj)
