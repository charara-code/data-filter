from .data_loader.factory import Factory
from .data_loader.xml_data_loader import XMLDataLoader

loader_name = "xml"    

filepath = "examples/example.xml"

xml_data_loader : XMLDataLoader = Factory.get_data_loader(loader_name=loader_name, data_source=filepath)

data = xml_data_loader.load_data()

data['flowerShop']['flower'][0]['name'] = "Dead Flower" # TODO: make it easier to access root and child tags

xml_data_loader.save_data(data)
print(data)

