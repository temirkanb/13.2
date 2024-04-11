from abc import ABC, abstractmethod


class PatternProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        return f"Экземпляр класса {self.__class__.__name__}"