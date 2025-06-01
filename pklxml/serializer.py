from lxml import etree
import inspect

def dump(obj, file_path):
    root = etree.Element("pklxml")
    _serialize(obj, root)
    tree = etree.ElementTree(root)
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding='utf-8')

def _serialize(obj, parent, name=None):
    if isinstance(obj, dict):
        dict_el = etree.SubElement(parent, "dict", name=name or "")
        for k, v in obj.items():
            item = etree.SubElement(dict_el, "item")
            key = etree.SubElement(item, "key", type=type(k).__name__)
            key.text = str(k)
            value = etree.SubElement(item, "value", type=type(v).__name__)
            if isinstance(v, (dict, list, tuple, object)):
                _serialize(v, value)
            else:
                value.text = str(v)

    elif isinstance(obj, list):
        list_el = etree.SubElement(parent, "list", name=name or "")
        for v in obj:
            item = etree.SubElement(list_el, "item", type=type(v).__name__)
            item.text = str(v)

    elif isinstance(obj, tuple):
        tuple_el = etree.SubElement(parent, "tuple", name=name or "")
        for v in obj:
            item = etree.SubElement(tuple_el, "item", type=type(v).__name__)
            item.text = str(v)

    elif inspect.isclass(type(obj)) and hasattr(obj, "__dict__"):
        class_el = etree.SubElement(parent, "class", name=type(obj).__name__, module=obj.__class__.__module__)
        for attr_name, attr_value in obj.__dict__.items():
            attr_el = etree.SubElement(class_el, "attribute", name=attr_name, type=type(attr_value).__name__)
            if isinstance(attr_value, (dict, list, tuple, object)):
                _serialize(attr_value, attr_el)
            else:
                attr_el.text = str(attr_value)

    else:
        var_el = etree.SubElement(parent, "variable", name=name or "value", type=type(obj).__name__)
        var_el.text = str(obj)
