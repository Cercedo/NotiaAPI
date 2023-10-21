from note.application.services.interfaces import ServiceInterface
from note.domain.entities import NoteEntity
from note.domain.repositories import NoteRepository


class CreateNoteService(ServiceInterface):
    def __init__(self, note_repository: NoteRepository):
        self._note_repository = note_repository

    def execute(self, note_entity: NoteEntity) -> NoteEntity:
        note = self._note_repository.create(note_entity)
        return note
