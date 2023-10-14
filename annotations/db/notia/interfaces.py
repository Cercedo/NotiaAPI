from abc import ABC, abstractmethod


class DBPopulatorInterface(ABC):
    """Blueprint class for creating DB populators."""

    @abstractmethod
    def execute(cls) -> None:
        raise NotImplementedError
