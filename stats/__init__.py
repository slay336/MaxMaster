from abc import ABC, abstractmethod


class BasicStat(ABC):
    _caption: str

    def __init__(self):
        pass

    @property
    @abstractmethod
    def caption(self):
        pass


class Knowledge(BasicStat):
    @property
    def caption(self):
        return self._caption


