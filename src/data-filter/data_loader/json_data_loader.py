from base_data_loader import BaseDataLoader
from models.data_containers.json_data_container import JsonDataContainer
import json


"""
JSON schemas accepted by the data loader

[
    {
        "field1": "value1",
        "field2": 2,
        "field3": 3.0,
        "field4": true,
        "field5": [1, 2, 3], # or any list that containes values of the types mentioned above (LIST OF LISTS OR LIST OF DICTS/OBJs NOT SUPPORTED)
    },
    {
        "field1": "value2",
        "field2": 3,
        "field3": 4.0,
        "field4": false,
        "field5": [4, 5, 6],
    },
    ...
]

"""

class JsonDataLoader(BaseDataLoader):

    def __init__(self, data_source):
        super().__init__(data_source)
        self.data = None
    
    def load_data(self):
        try :
            with open(self.data_source, 'r', encoding="utf-8") as file:
                return JsonDataContainer(json.load(file))
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            self.data = None

    def save_data(self, data : JsonDataContainer):
        try:
            with open(self.data_source, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            self.data = None

    def __repr__(self):
        return f"Data @ {self.data_source})"
    
    def __str__(self):
        return f"Data @ {self.data_source}"
    
    
    
