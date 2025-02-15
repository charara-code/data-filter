import pandas as pd
from typing import Dict, Any


class CSVStats:

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def get_numeric_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get statistics for numeric columns (min, max, average).

        :return: A dictionary with statistics for each numeric column.
        """
        numeric_stats = {}
        numeric_columns = self.dataframe.select_dtypes(include=['number']).columns

        for column in numeric_columns:
            numeric_stats[column] = {
                'min': self.dataframe[column].min(),
                'max': self.dataframe[column].max(),
                'average': self.dataframe[column].mean()
            }

        return numeric_stats

    def get_boolean_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get statistics for boolean columns (% true and % false).

        :return: A dictionary with statistics for each boolean column.
        """
        boolean_stats = {}
        boolean_columns = self.dataframe.select_dtypes(include=['bool']).columns

        for column in boolean_columns:
            true_count = self.dataframe[column].sum()
            false_count = len(self.dataframe) - true_count
            total = len(self.dataframe)
            boolean_stats[column] = {
                'true_percentage': (true_count / total) * 100,
                'false_percentage': (false_count / total) * 100
            }

        return boolean_stats

    def get_list_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get statistics for list columns (min, max, average size).

        :return: A dictionary with statistics for each list column.
        """
        list_stats = {}
        list_columns = self.dataframe.select_dtypes(include=['object']).columns

        for column in list_columns:
            if self.dataframe[column].apply(lambda x: isinstance(x, list)).all():
                sizes = self.dataframe[column].apply(len)
                list_stats[column] = {
                    'min_size': sizes.min(),
                    'max_size': sizes.max(),
                    'average_size': sizes.mean()
                }

        return list_stats

    def get_all_stats(self) -> Dict[str, Any]:
        """
        Get all statistics for numeric, boolean, and list columns.

        :return: A dictionary with all statistics.
        """
        return {
            'numeric_stats': self.get_numeric_stats(),
            'boolean_stats': self.get_boolean_stats(),
            'list_stats': self.get_list_stats()
        }

    def __repr__(self):
        return f"CSVStats(dataframe={self.dataframe})"

    def __str__(self):
        return f"CSVStats with {len(self.dataframe)} rows"


if __name__ == "__main__":
    data = {
        'field1': ['value1', 'value2', 'value3'],
        'field2': [10, 8, 1],
        'field3': [3.0, 7.0, 5.0],
        'field4': [True, False, True],
        'field5': [[99, 2, 3], [59, 5, 6], [9, 8, 9]]
    }
    df = pd.DataFrame(data)

    stats = CSVStats(df)
    all_stats = stats.get_all_stats()

    print(all_stats)