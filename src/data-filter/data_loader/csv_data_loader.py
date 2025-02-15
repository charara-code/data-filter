from .base_data_loader import BaseDataLoader
from ..models.data_containers.csv_data_container import CSVDataContainer
import pandas as pd
import os, logging


class CSVDataLoader(BaseDataLoader):
    """
    CSVDataLoader is responsible for loading and saving CSV data from/to a specified file.

    Attributes:
        data_source (str): The path to the CSV file to load data from or save data to.

    Methods:
        load_data() -> pd.DataFrame:
            Loads data from the CSV file specified by data_source and returns it as a pandas DataFrame.
        
        save_data(data: pd.DataFrame):
            Saves the given pandas DataFrame to the CSV file specified by data_source.
    """

    def __init__(self, data_source):
        """
        Initializes the CSVDataLoader with the specified data source.

        Args:
            data_source (str): The path to the CSV file to load data from or save data to.
        """
        super().__init__(data_source)


    def load_data(self) -> pd.DataFrame:
        """
        Loads data from the CSV file specified by data_source and returns it as a pandas DataFrame.

        Returns:
            pd.DataFrame: The loaded data.

        Raises:
            FileNotFoundError: If the CSV file specified by data_source is not found.
            Exception: If there is an error loading the data.
        """
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
        """
        Saves the given pandas DataFrame to the CSV file specified by data_source.

        Args:
            data (pd.DataFrame): The data to save.

        Raises:
            ValueError: If the data is not a pandas DataFrame.
            FileNotFoundError: If the CSV file specified by data_source is not found.
            Exception: If there is an error saving the data.
        """
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
        """
        Returns a string representation of the CSVDataLoader object.

        Returns:
            str: A string representation of the CSVDataLoader object.
        """
        return f"Data @ {self.data_source})"
    
    def __str__(self):
        """
        Returns a string representation of the CSVDataLoader object.

        Returns:
            str: A string representation of the CSVDataLoader object.
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
            data_source (str): The path to the CSV file to load data from or save data to.

        Raises:
            ValueError: If the data source is not a string path to a CSV file.
            FileNotFoundError: If the CSV file specified by data_source is not found.
        """
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