from .data_loader.factory import Factory
from .data_loader.csv_data_loader import CSVDataLoader
from .data_loader.json_data_loader import JsonDataLoader
from .sorter.json_sorter import JsonSorter
from.sorter.csv_sorter import CSVSorter

loader_name = "json"    

filepath = "examples/example.json"

json_data_loader : JsonDataLoader = Factory.get_data_loader(loader_name=loader_name, data_source=filepath)

json_data = json_data_loader.load_data()

# sorter = JsonSorter(data)

# sorter.sort_by_key("field1")

# data["Name"][0] = "BLAH BALAH"

# json_data_loader.save_data(data)

# print(data["Name"])

csv_loader_name = "csv"
csv_filepath = "examples/example.csv"
csv_data_loader : CSVDataLoader = Factory.get_data_loader(loader_name=csv_loader_name, data_source=csv_filepath)
df = csv_data_loader.load_data()

sorter = CSVSorter(df)
sorter.sort_by_multiple_columns(columns=["Age", "Grade"], ascending=[True, False])

sorted_df = sorter.get_sorted_dataframe()

print(sorted_df)


