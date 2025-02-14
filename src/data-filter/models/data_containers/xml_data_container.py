from pydantic import BaseModel
from collections import defaultdict
import xml.etree.ElementTree as ET

class XMLDataContainer(BaseModel):


    @staticmethod
    def _as_py_dict(xml_file_path) -> dict:

        def xml_to_dict(element):
            if len(element) == 0:
                return element.text
            result = defaultdict(list)
            for child in element:
                result[child.tag].append(xml_to_dict(child))
            return {k: v if len(v) > 1 else v[0] for k, v in result.items()}
    
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        xml_dict = {root.tag: xml_to_dict(root)}
        
        return xml_dict
    

    @staticmethod
    def _from_py_dict(data: dict, xml_file_path):
        def dict_to_xml(tag, d):
            elem = ET.Element(tag)
            if isinstance(d, dict):
                for key, val in d.items():
                    child = dict_to_xml(key, val)
                    elem.append(child)
            elif isinstance(d, list):
                for item in d:
                    child = dict_to_xml(tag, item)
                    elem.append(child)
            else:
                elem.text = str(d)
            return elem

        root_tag = list(data.keys())[0]
        root_element = dict_to_xml(root_tag, data[root_tag])
        tree = ET.ElementTree(root_element)
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)