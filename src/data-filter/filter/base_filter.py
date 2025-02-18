from abc import ABC, abstractmethod
from typing import Any, List


class BaseFilter(ABC):

    @abstractmethod
    def filter_by_string_contains(self, column: str, substring: str):
        """
        Filter by checking if the string value contains the substring.

        :param column: The column to filter by.
        :param substring: The substring to check for.
        """
        pass

    @abstractmethod
    def filter_by_string_startswith(self, column: str, prefix: str):
        """
        Filter by checking if the string value starts with the prefix.

        :param column: The column to filter by.
        :param prefix: The prefix to check for.
        """
        pass

    @abstractmethod
    def filter_by_string_endswith(self, column: str, suffix: str):
        """
        Filter by checking if the string value ends with the suffix.

        :param column: The column to filter by.
        :param suffix: The suffix to check for.
        """
        pass

    @abstractmethod
    def filter_by_list_all_elements(self, column: str, elements: List[Any]):
        """
        Filter by checking if all elements are in the list value.

        :param column: The column to filter by.
        :param elements: The elements to check for.
        """
        pass

    @abstractmethod
    def filter_by_list_min(self, column: str, min_value: Any):
        """
        Filter by checking if the minimum value in the list is greater than or equal to min_value.

        :param column: The column to filter by.
        :param min_value: The minimum value to compare against.
        """
        pass

    @abstractmethod
    def filter_by_list_max(self, column: str, max_value: Any):
        """
        Filter by checking if the maximum value in the list is less than or equal to max_value.

        :param column: The column to filter by.
        :param max_value: The maximum value to compare against.
        """
        pass

    @abstractmethod
    def filter_by_list_average(
        self, column: str, avg_value: float, comparison: str = "eq"
    ):
        """
        Filter by checking if the average value in the list meets the comparison criteria.

        :param column: The column to filter by.
        :param avg_value: The average value to compare against.
        :param comparison: The type of comparison ('eq', 'lt', 'gt').
        """
        pass
