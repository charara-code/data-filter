from .base_data_loader import BaseDataLoader
from ..models.data_containers.json_data_container import JsonDataContainer
import json, os, logging


class JsonDataLoader(BaseDataLoader):
    """
    JsonDataLoader is responsible for loading and saving JSON data from/to a specified file.

    Attributes:
        data_source (str): The path to the JSON file to load data from or save data to.

    Methods:
        load_data() -> JsonDataContainer:
            Loads data from the JSON file specified by data_source and returns it as a JsonDataContainer object.
        
        save_data(data: JsonDataContainer):
            Saves the given JsonDataContainer object to the JSON file specified by data_source.
    """

    def __init__(self, data_source):
        """
        Initializes the JsonDataLoader with the specified data source.

        Args:
            data_source (str): The path to the JSON file to load data from or save data to.
        """
        super().__init__(data_source)
        
    
    def load_data(self) -> JsonDataContainer:
        """
        Loads data from the JSON file specified by data_source and returns it as a JsonDataContainer object.

        Returns:
            JsonDataContainer: The loaded data.

        Raises:
            FileNotFoundError: If the JSON file specified by data_source is not found.
            Exception: If there is an error loading the data.
        """
        try :
            with open(self.data_source, 'r', encoding="utf-8") as file:
                data = JsonDataContainer(data=json.load(file)["data"])
                logging.info(f"Data loaded from {self.data_source}")
                return data
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            print(f"File not found: {e}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            print(f"Error loading data: {e}")
            
            

    def save_data(self, data : JsonDataContainer):
        """
        Saves the given JsonDataContainer object to the JSON file specified by data_source.

        Args:
            data (JsonDataContainer): The data to save.

        Raises:
            ValueError: If the data is not a JsonDataContainer object.
            FileNotFoundError: If the JSON file specified by data_source is not found.
            Exception: If there is an error saving the data.
        """
        if not isinstance(data, JsonDataContainer):
            raise ValueError("Data must be a JsonDataContainer object")
        if not os.path.exists(self.data_source):
            raise FileNotFoundError(f"File not found: {self.data_source}")
        try:
            with open(self.data_source, 'w', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            logging.error(f"Error saving data: {e}")
            print(f"Error saving data: {e}")
            

    def __repr__(self):
        """
        Returns a string representation of the JsonDataLoader object.

        Returns:
            str: A string representation of the JsonDataLoader object.
        """
        return f"Data @ {self.data_source})"
    
    def __str__(self):
        """
        Returns a string representation of the JsonDataLoader object.

        Returns:
            str: A string representation of the JsonDataLoader object.
        """
        return f"Data @ {self.data_source}"
    

    def _get_data_source(self):
        """
        Gets the data source.

        Returns:
            str: The data source.
        """
        return self._data_source
    
    def _set_data_source(self, data_source):
        """
        Sets the data source.

        Args:
            data_source (str): The path to the JSON file to load data from or save data to.

        Raises:
            ValueError: If the data source is not a string path to a JSON file.
            FileNotFoundError: If the JSON file specified by data_source is not found.
        """
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
    
    
    
