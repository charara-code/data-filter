from .base_data_loader import BaseDataLoader
from ..models.data_containers.csv_data_container import CSVDataContainer
import pandas as pd
import os, logging


class CSVDataLoader(BaseDataLoader):

    def __init__(self, data_source):
        super().__init__(data_source)


    def load_data(self) -> pd.DataFrame:

        try:
            data = CSVDataContainer._as_pandas_data_frame(data_source=self.data_source)
            logging.info(f"Data loaded from {self.data_source}")
            return data
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            print(f"File not found: {e}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            print(f"Error loading data: {e}")



    def save_data(self, data: pd.DataFrame):
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")
        if not os.path.exists(self.data_source):
            raise FileNotFoundError(f"File not found: {self.data_source}")
        try:
            data.to_csv(self.data_source, index=False)
            logging.info(f"Data saved to {self.data_source}")
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
            raise ValueError("Data source must be a string path to a CSV file")
        # make sure the path exists
        if not os.path.exists(data_source):
            raise FileNotFoundError(f"File not found: {data_source}")
        # make sure it is a csv file
        if not data_source.endswith('.csv'):
            raise ValueError("Only CSV files are supported for the CSV data loader")
        self._data_source = data_source




    data_source = property(_get_data_source, _set_data_source)