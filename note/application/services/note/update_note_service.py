from note.application.services.interfaces import ServiceInterface
from note.domain.entities import NoteEntity
from note.domain.repositories import NoteRepository


class UpdateNoteService(ServiceInterface):
    def __init__(self, note_repository: NoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, id: int, note_entity) -> NoteEntity:
        note = self._note_repository.update(id, note_entity)
        return note
