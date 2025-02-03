from base_data_loader import BaseDataLoader
from models.data_containers.json_data_container import JsonDataContainer
import json, os, logging


class JsonDataLoader(BaseDataLoader):

    def __init__(self, data_source):
        super().__init__(data_source)
        
    
    def load_data(self) -> JsonDataContainer:
        try :
            with open(self.data_source, 'r', encoding="utf-8") as file:
                data = JsonDataContainer(json.load(file))
                logging.info(f"Data loaded from {self.data_source}")
                return data
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            print(f"File not found: {e}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            print(f"Error loading data: {e}")
            
            

    def save_data(self, data : JsonDataContainer):
        try:
            with open(self.data_source, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            print(f"File not found: {e}")

        except Exception as e:
            logging.error(f"Error saving data: {e}")
            print(f"Error saving data: {e}")
            

    def __repr__(self):
        return f"Data @ {self.data_source})"
    
    def __str__(self):
        return f"Data @ {self.data_source}"
    

    def _get_data_source(self):
        return self._data_source
    
    def _set_data_source(self, data_source):
        if not isinstance(data_source, str):
            raise ValueError("Data source must be a string path to a JSON file")
        # make sure the path exists
        if not os.path.exists(data_source):
            raise FileNotFoundError(f"File not found: {data_source}")
        # make sure it is a json file
        if not data_source.endswith('.json'):
            raise ValueError("Only JSON files are supported for the json data loader")
        self._data_source = data_source


    data_source = property(_get_data_source, _set_data_source)
    
    
    
