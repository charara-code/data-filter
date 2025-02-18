from ..models.data_containers.json_data_container import JsonDataContainer
from typing import Any, List
from .base_filter import BaseFilter


class JSONFilter(BaseFilter):

    def __init__(self, data_container: JsonDataContainer):
        self.data_container = data_container

    def filter_by_key(self, key: str, value: Any, comparison: str = "eq"):
        """
        Filter the data container by a specific key and value.

        :param key: The key to filter by.
        :param value: The value to compare against.
        :param comparison: The type of comparison ('eq', 'lt', 'gt').
        """
        if comparison not in ["eq", "lt", "gt"]:
            raise ValueError("Comparison must be 'eq', 'lt', or 'gt'")

        filtered_data = []
        for item in self.data_container.data:
            item_value = item.item.get(key)
            if self._compare(item_value, value, comparison):
                filtered_data.append(item)

        self.data_container.data = filtered_data

    def filter_by_string_contains(self, key: str, substring: str):
        """
        Filter the data container by checking if the string value contains the substring.

        :param key: The key to filter by.
        :param substring: The substring to check for.
        """
        filtered_data = [
            item
            for item in self.data_container.data
            if substring in item.item.get(key, "")
        ]
        self.data_container.data = filtered_data

    def filter_by_string_startswith(self, key: str, prefix: str):
        """
        Filter the data container by checking if the string value starts with the prefix.

        :param key: The key to filter by.
        :param prefix: The prefix to check for.
        """
        filtered_data = [
            item
            for item in self.data_container.data
            if item.item.get(key, "").startswith(prefix)
        ]
        self.data_container.data = filtered_data

    def filter_by_string_endswith(self, key: str, suffix: str):
        """
        Filter the data container by checking if the string value ends with the suffix.

        :param key: The key to filter by.
        :param suffix: The suffix to check for.
        """
        filtered_data = [
            item
            for item in self.data_container.data
            if item.item.get(key, "").endswith(suffix)
        ]
        self.data_container.data = filtered_data

    def filter_by_list_all_elements(self, key: str, elements: List[Any]):
        """
        Filter the data container by checking if all elements are in the list value.

        :param key: The key to filter by.
        :param elements: The elements to check for.
        """
        filtered_data = [
            item
            for item in self.data_container.data
            if all(elem in item.item.get(key, []) for elem in elements)
        ]
        self.data_container.data = filtered_data

    def filter_by_list_min(self, key: str, min_value: Any):
        """
        Filter the data container by checking if the minimum value in the list is greater than or equal to min_value.

        :param key: The key to filter by.
        :param min_value: The minimum value to compare against.
        """
        filtered_data = [
            item
            for item in self.data_container.data
            if min(item.item.get(key, [])) >= min_value
        ]
        self.data_container.data = filtered_data

    def filter_by_list_max(self, key: str, max_value: Any):
        """
        Filter the data container by checking if the maximum value in the list is less than or equal to max_value.

        :param key: The key to filter by.
        :param max_value: The maximum value to compare against.
        """
        filtered_data = [
            item
            for item in self.data_container.data
            if max(item.item.get(key, [])) <= max_value
        ]
        self.data_container.data = filtered_data

    def filter_by_list_average(
        self, key: str, avg_value: float, comparison: str = "eq"
    ):
        """
        Filter the data container by checking if the average value in the list meets the comparison criteria.

        :param key: The key to filter by.
        :param avg_value: The average value to compare against.
        :param comparison: The type of comparison ('eq', 'lt', 'gt').
        """
        filtered_data = []
        for item in self.data_container.data:
            list_value = item.item.get(key, [])
            if list_value:
                avg = sum(list_value) / len(list_value)
                if self._compare(avg, avg_value, comparison):
                    filtered_data.append(item)

        self.data_container.data = filtered_data

    def _compare(self, item_value: Any, value: Any, comparison: str) -> bool:
        """
        Helper function to compare values based on the specified comparison type.

        :param item_value: The value from the item.
        :param value: The value to compare against.
        :param comparison: The type of comparison ('eq', 'lt', 'gt').
        :return: The result of the comparison.
        """
        if isinstance(item_value, list):
            item_value = len(item_value)
        if isinstance(value, list):
            value = len(value)

        if comparison == "eq":
            return item_value == value
        elif comparison == "lt":
            return item_value < value
        elif comparison == "gt":
            return item_value > value

    def get_filtered_data(self) -> JsonDataContainer:
        """
        Get the filtered data container.

        :return: The filtered JsonDataContainer.
        """
        return self.data_container

    def __repr__(self):
        return f"JSONFilter(data_container={self.data_container})"

    def __str__(self):
        return f"JSONFilter with {len(self.data_container)} items"


if __name__ == "__main__":
    from ..data_loader.json_data_loader import JsonDataLoader

    data_loader = JsonDataLoader(data_source="examples/example.json")
    data_container = data_loader.load_data()

    filterer = JSONFilter(data_container)
    filterer.filter_by_key("field2", 5, comparison="gt")
    filtered_data = filterer.get_filtered_data()

    print(filtered_data)
