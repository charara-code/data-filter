import pandas as pd
from typing import Any, List


class CSVFilter:

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def filter_by_column(self, column: str, value: Any, comparison: str = 'eq'):
        """
        Filter the DataFrame by a specific column and value.

        :param column: The column to filter by.
        :param value: The value to compare against.
        :param comparison: The type of comparison ('eq', 'lt', 'gt').
        """
        if comparison not in ['eq', 'lt', 'gt']:
            raise ValueError("Comparison must be 'eq', 'lt', or 'gt'")

        if comparison == 'eq':
            self.dataframe = self.dataframe[self.dataframe[column] == value]
        elif comparison == 'lt':
            self.dataframe = self.dataframe[self.dataframe[column] < value]
        elif comparison == 'gt':
            self.dataframe = self.dataframe[self.dataframe[column] > value]

    def filter_by_string_contains(self, column: str, substring: str):
        """
        Filter the DataFrame by checking if the string value contains the substring.

        :param column: The column to filter by.
        :param substring: The substring to check for.
        """
        self.dataframe = self.dataframe[self.dataframe[column].str.contains(substring, na=False)]

    def filter_by_string_startswith(self, column: str, prefix: str):
        """
        Filter the DataFrame by checking if the string value starts with the prefix.

        :param column: The column to filter by.
        :param prefix: The prefix to check for.
        """
        self.dataframe = self.dataframe[self.dataframe[column].str.startswith(prefix, na=False)]

    def filter_by_string_endswith(self, column: str, suffix: str):
        """
        Filter the DataFrame by checking if the string value ends with the suffix.

        :param column: The column to filter by.
        :param suffix: The suffix to check for.
        """
        self.dataframe = self.dataframe[self.dataframe[column].str.endswith(suffix, na=False)]

    def filter_by_list_all_elements(self, column: str, elements: List[Any]):
        """
        Filter the DataFrame by checking if all elements are in the list value.

        :param column: The column to filter by.
        :param elements: The elements to check for.
        """
        self.dataframe = self.dataframe[self.dataframe[column].apply(lambda x: all(elem in x for elem in elements))]

    def filter_by_list_min(self, column: str, min_value: Any):
        """
        Filter the DataFrame by checking if the minimum value in the list is greater than or equal to min_value.

        :param column: The column to filter by.
        :param min_value: The minimum value to compare against.
        """
        self.dataframe = self.dataframe[self.dataframe[column].apply(lambda x: min(x) >= min_value)]

    def filter_by_list_max(self, column: str, max_value: Any):
        """
        Filter the DataFrame by checking if the maximum value in the list is less than or equal to max_value.

        :param column: The column to filter by.
        :param max_value: The maximum value to compare against.
        """
        self.dataframe = self.dataframe[self.dataframe[column].apply(lambda x: max(x) <= max_value)]

    def filter_by_list_average(self, column: str, avg_value: float, comparison: str = 'eq'):
        """
        Filter the DataFrame by checking if the average value in the list meets the comparison criteria.

        :param column: The column to filter by.
        :param avg_value: The average value to compare against.
        :param comparison: The type of comparison ('eq', 'lt', 'gt').
        """
        if comparison not in ['eq', 'lt', 'gt']:
            raise ValueError("Comparison must be 'eq', 'lt', or 'gt'")

        if comparison == 'eq':
            self.dataframe = self.dataframe[self.dataframe[column].apply(lambda x: sum(x) / len(x) == avg_value)]
        elif comparison == 'lt':
            self.dataframe = self.dataframe[self.dataframe[column].apply(lambda x: sum(x) / len(x) < avg_value)]
        elif comparison == 'gt':
            self.dataframe = self.dataframe[self.dataframe[column].apply(lambda x: sum(x) / len(x) > avg_value)]

    def get_filtered_dataframe(self) -> pd.DataFrame:
        """
        Get the filtered DataFrame.

        :return: The filtered DataFrame.
        """
        return self.dataframe

    def __repr__(self):
        return f"CSVFilter(dataframe={self.dataframe})"

    def __str__(self):
        return f"CSVFilter with {len(self.dataframe)} rows"


# Example usage
if __name__ == "__main__":
    # Example DataFrame
    data = {
        'field1': ['value1', 'value2', 'value3'],
        'field2': [10, 8, 1],
        'field3': [3.0, 7.0, 5.0],
        'field4': [True, False, True],
        'field5': [[99, 2, 3], [59, 5, 6], [9, 8, 9]]
    }
    df = pd.DataFrame(data)

    filterer = CSVFilter(df)
    filterer.filter_by_column('field2', 5, comparison='gt')
    filtered_df = filterer.get_filtered_dataframe()

    print(filtered_df)