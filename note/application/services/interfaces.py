from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError
