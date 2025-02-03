
from data_loader.json_data_loader import JsonDataLoader
from data_loader.base_data_loader import BaseDataLoader


class Factory:


    @staticmethod
    def get_data_loader(data_source: str) -> BaseDataLoader:
        if data_source.endswith('.json'):
            return JsonDataLoader(data_source)
        else:
            raise ValueError(f"Data source not supported: {data_source}")