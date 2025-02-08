
from ..data_loader.json_data_loader import JsonDataLoader
from ..data_loader.base_data_loader import BaseDataLoader


class Factory:


    @staticmethod
    def get_data_loader(loader_name: str, data_source: str) -> BaseDataLoader:
        if loader_name == "json":
            return JsonDataLoader(data_source=data_source)
        else:
            raise ValueError(f"Data source not supported: {data_source}")