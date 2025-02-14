from .data_loader.factory import Factory
from .data_loader.csv_data_loader import CSVDataLoader

loader_name = "csv"    

filepath = "examples/example.csv"

csv_data_loader : CSVDataLoader = Factory.get_data_loader(loader_name=loader_name, data_source=filepath)

data = csv_data_loader.load_data()



data["Name"][0] = "BLAH BALAH"

csv_data_loader.save_data(data)

print(data["Name"])