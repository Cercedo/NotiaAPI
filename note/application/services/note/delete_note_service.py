from note.application.services.interfaces import ServiceInterface
from note.domain.repositories import NoteRepository


class DeleteNoteService(ServiceInterface):
    def __init__(self, note_repository: NoteRepository) -> None:
        self._note_repository = note_repository

    def execute(self, id: int) -> int:
        self._note_repository.delete(id)
        return id
