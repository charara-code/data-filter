from pydantic import BaseModel
from typing import List, Dict, Union


class JsonDataItem(BaseModel):
    """
    Class to represent a single JSON data item.
    types can be str, int, float, bool, or a list of str, int, float, or bool.
    """

    item: Dict[str, Union[str, int, float, bool, List[Union[str, int, float, bool]]]]


class JsonDataContainer(BaseModel):
    """
    Class to represent a container for JSON data items.
    """

    data: List[JsonDataItem]

    def __getitem__(self, index: int) -> JsonDataItem:
        """
        Method to get the i-th element using the [] notation.

        :param index: The index of the element to retrieve.
        :return: The JsonDataItem at the specified index.
        """
        return self.data[index].item

    def __setitem__(self, index: int, value: JsonDataItem):
        """
        Method to set the i-th element using the [] notation.

        :param index: The index of the element to set.
        :param value: The JsonDataItem to set at the specified index.
        """
        self.data[index].item = value

    def __len__(self):
        """
        Method to get the length of the data container.

        :return: The length of the data container.
        """
        return len(self.data)
