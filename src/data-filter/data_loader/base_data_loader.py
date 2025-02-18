from abc import ABC, abstractmethod


class BaseDataLoader(ABC):

    def __init__(self, data_source):
        self.data_source = data_source

    @abstractmethod
    def load_data(self):
        pass
