from note.application.services.interfaces import ServiceInterface
from note.domain.entities import NoteEntity
from note.domain.repositories import NoteRepository


class GetNoteService(ServiceInterface):
    def __init__(self, note_repository: NoteRepository):
        self._note_repository = note_repository

    def execute(self, id: int) -> NoteEntity:
        note = self._note_repository.get(id)
        return note
