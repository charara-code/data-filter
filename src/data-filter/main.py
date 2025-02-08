from .data_loader.factory import Factory


loader_name = "json"    

filepath = "examples/example.json"

json_data_loader = Factory.get_data_loader(loader_name=loader_name, data_source=filepath)

data = json_data_loader.load_data()


data[0] = 1


print(data)