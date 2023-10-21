from typing import List, cast

from note.domain.entities import NoteEntity
from note.domain.repositories import NoteRepository
from note.infrastructure.orms.models import Note


class PostgresNoteRepository(NoteRepository):
    def list(self) -> List[NoteEntity]:
        note_queryset = Note.objects.all().values()
        note_list = list(note_queryset)
        return cast(List[NoteEntity], note_list)

    def create(self, note_entity: NoteEntity) -> NoteEntity:
        data = note_entity.to_dict()
        note = Note.objects.create(**data)
        return note.to_entity()

    def get(self, id: int) -> NoteEntity:
        note = Note.objects.get(id=id)
        return note.to_entity()

    def update(self, id: int, note_entity: NoteEntity) -> NoteEntity:
        data = note_entity.to_dict()
        Note.objects.filter(id=id).update(**data)
        return note_entity

    def delete(self, id: int) -> int:
        Note.objects.get(id=id).delete()
        return id
