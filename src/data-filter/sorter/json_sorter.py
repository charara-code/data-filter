from ..models.data_containers.json_data_container import JsonDataContainer
from typing import List
from .base_sorter import BaseSorter


class JsonSorter(BaseSorter):

    def __init__(self, data_container: JsonDataContainer):
        self.data_container = data_container

    def sort_by_key(self, key: str, reverse: bool = False):
        """
        Sort the data container by a specific key.

        :param key: The key to sort by.
        :param reverse: Whether to sort in descending order.
        """
        self.data_container.data.sort(
            key=lambda item: self._get_sort_key(item.item.get(key)), reverse=reverse
        )

    def sort_by_multiple_keys(self, keys: List[str], reverse: bool = False):
        """
        Sort the data container by multiple keys.

        :param keys: The list of keys to sort by.
        :param reverse: Whether to sort in descending order.
        """
        self.data_container.data.sort(
            key=lambda item: tuple(
                self._get_sort_key(item.item.get(key)) for key in keys
            ),
            reverse=reverse,
        )

    def _get_sort_key(self, value):
        """
        Helper function to get the sort key.

        :param value: The value to get the sort key from.
        :return: The sort key.
        """
        if isinstance(value, list):
            return value[0] if value else None
        return value

    def get_sorted_data(self) -> JsonDataContainer:
        """
        Get the sorted data container.

        :return: The sorted JsonDataContainer.
        """
        return self.data_container

    def __repr__(self):
        return f"JSONSorter(data_container={self.data_container})"

    def __str__(self):
        return f"JSONSorter with {len(self.data_container)} items"


if __name__ == "__main__":
    from ..data_loader.json_data_loader import JsonDataLoader

    data_loader = JsonDataLoader(data_source="examples/example.json")
    data_container = data_loader.load_data()

    sorter = JsonSorter(data_container)
    sorter.sort_by_multiple_keys(keys=["field3", "field5"], reverse=True)
    sorted_data = sorter.get_sorted_data()

    print(sorted_data)
