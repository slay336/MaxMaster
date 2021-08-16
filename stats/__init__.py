from abc import ABC, abstractmethod


class BasicStat(ABC):
    _name: str
    _caption: str

    def __init__(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    @name.setter
    def name(self, value):
        pass
