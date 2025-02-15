from .data_loader.factory import Factory
from .data_loader.csv_data_loader import CSVDataLoader
from .data_loader.json_data_loader import JsonDataLoader
from .sorter.json_sorter import JsonSorter

loader_name = "json"    

filepath = "examples/example.json"

json_data_loader : JsonDataLoader = Factory.get_data_loader(loader_name=loader_name, data_source=filepath)

data = json_data_loader.load_data()

sorter = JsonSorter(data)

sorter.sort_by_key("field1")

# data["Name"][0] = "BLAH BALAH"

# json_data_loader.save_data(data)

# print(data["Name"])