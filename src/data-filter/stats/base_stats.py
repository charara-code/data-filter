from abc import ABC, abstractmethod



class BaseStats(ABC):

    @abstractmethod
    def get_numeric_stats(self):
        pass


    @abstractmethod
    def get_boolean_stats(self):
        pass


    @abstractmethod
    def get_list_stats(self):
        pass


    @abstractmethod
    def get_all_stats(self):
        pass
    

    