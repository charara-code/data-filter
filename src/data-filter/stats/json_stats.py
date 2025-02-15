from ..models.data_containers.json_data_container import JsonDataContainer
from typing import Dict, Any
import numpy as np


class JSONStats:

    def __init__(self, data_container: JsonDataContainer):
        self.data_container = data_container

    def get_numeric_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get statistics for numeric fields (min, max, average).

        :return: A dictionary with statistics for each numeric field.
        """
        numeric_stats = {}
        for item in self.data_container.data:
            for key, value in item.item.items():
                if isinstance(value, (int, float)):
                    if key not in numeric_stats:
                        numeric_stats[key] = []
                    numeric_stats[key].append(value)
                elif isinstance(value, list) and all(isinstance(i, (int, float)) for i in value):
                    if key not in numeric_stats:
                        numeric_stats[key] = []
                    numeric_stats[key].append(len(value))

        stats = {}
        for key, values in numeric_stats.items():
            stats[key] = {
                'min': np.min(values),
                'max': np.max(values),
                'average': np.mean(values)
            }
        return stats

    def get_boolean_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get statistics for boolean fields (% true and % false).

        :return: A dictionary with statistics for each boolean field.
        """
        boolean_stats = {}
        for item in self.data_container.data:
            for key, value in item.item.items():
                if isinstance(value, bool):
                    if key not in boolean_stats:
                        boolean_stats[key] = {'true': 0, 'false': 0}
                    if value:
                        boolean_stats[key]['true'] += 1
                    else:
                        boolean_stats[key]['false'] += 1

        stats = {}
        for key, counts in boolean_stats.items():
            total = counts['true'] + counts['false']
            stats[key] = {
                'true_percentage': (counts['true'] / total) * 100,
                'false_percentage': (counts['false'] / total) * 100
            }
        return stats

    def get_list_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Get statistics for list fields (min, max, average size).

        :return: A dictionary with statistics for each list field.
        """
        list_stats = {}
        for item in self.data_container.data:
            for key, value in item.item.items():
                if isinstance(value, list):
                    if key not in list_stats:
                        list_stats[key] = []
                    list_stats[key].append(len(value))

        stats = {}
        for key, values in list_stats.items():
            stats[key] = {
                'min_size': np.min(values),
                'max_size': np.max(values),
                'average_size': np.mean(values)
            }
        return stats

    def get_all_stats(self) -> Dict[str, Any]:
        """
        Get all statistics for numeric, boolean, and list fields.

        :return: A dictionary with all statistics.
        """
        return {
            'numeric_stats': self.get_numeric_stats(),
            'boolean_stats': self.get_boolean_stats(),
            'list_stats': self.get_list_stats()
        }

    def __repr__(self):
        return f"JSONStats(data_container={self.data_container})"

    def __str__(self):
        return f"JSONStats with {len(self.data_container)} items"


if __name__ == "__main__":
    from ..data_loader.json_data_loader import JsonDataLoader

    data_loader = JsonDataLoader(data_source="examples/example.json")
    data_container = data_loader.load_data()

    stats = JSONStats(data_container)
    all_stats = stats.get_all_stats()

    print(all_stats)