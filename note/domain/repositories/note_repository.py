from abc import ABC, abstractmethod
from typing import List

from note.domain.entities import NoteEntity


class NoteRepository(ABC):
    @abstractmethod
    def list(self) -> List[NoteEntity]:
        raise NotImplementedError

    @abstractmethod
    def create(self, note_entity: NoteEntity) -> NoteEntity:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int) -> NoteEntity:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, note_entity: NoteEntity) -> NoteEntity:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> int:
        raise NotImplementedError
