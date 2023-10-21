from typing import List

from note.application.services.interfaces import ServiceInterface
from note.domain.entities import NoteEntity
from note.domain.repositories import NoteRepository


class ListNoteService(ServiceInterface):
    def __init__(self, note_repository: NoteRepository):
        self._note_repository = note_repository

    def execute(self) -> List[NoteEntity]:
        note_list = self._note_repository.list()
        return note_list
