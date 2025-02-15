import pandas as pd
from typing import List
from .base_sorter import BaseSorter 

class CSVSorter(BaseSorter):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def sort_by_column(self, column: str, ascending: bool = True):
        """
        Sort the DataFrame by a specific column.

        :param column: The column to sort by.
        :param ascending: Whether to sort in ascending order.
        """
        self.dataframe = self.dataframe.sort_values(by=column, ascending=ascending)

    def sort_by_multiple_columns(self, columns: List[str], ascending: List[bool] = None):
        """
        Sort the DataFrame by multiple columns.

        :param columns: The list of columns to sort by.
        :param ascending: List of booleans indicating sort order for each column.
        """
        if ascending is None:
            ascending = [True] * len(columns)
        self.dataframe = self.dataframe.sort_values(by=columns, ascending=ascending)

    def get_sorted_dataframe(self) -> pd.DataFrame:
        """
        Get the sorted DataFrame.

        :return: The sorted DataFrame.
        """
        return self.dataframe

    def __repr__(self):
        return f"CSVSorter(dataframe={self.dataframe})"

    def __str__(self):
        return f"CSVSorter with {len(self.dataframe)} rows"


if __name__ == "__main__":
    data = {
        'field1': ['value1', 'value2', 'value3'],
        'field2': [10, 8, 1],
        'field3': [3.0, 7.0, 5.0],
        'field4': [True, False, True],
        'field5': [[99, 2, 3], [59, 5, 6], [9, 8, 9]]
    }
    df = pd.DataFrame(data)

    sorter = CSVSorter(df)
    sorter.sort_by_column('field2')
    sorted_df = sorter.get_sorted_dataframe()

    print(sorted_df)