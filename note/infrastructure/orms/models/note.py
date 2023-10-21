from django.db import models

from note.domain.entities import NoteEntity

from .utils import get_background_image_path


class Note(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.TextField()
    emoji = models.CharField(max_length=4, null=True)
    background_image = models.ImageField(
        upload_to=get_background_image_path, null=True
    )
    background_color = models.CharField(max_length=7, null=True)
    is_favorite = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_entity(self) -> NoteEntity:
        field_dict = {
            field.name: getattr(self, field.name)
            for field in self._meta.get_fields()
        }
        return NoteEntity(**field_dict)

    @staticmethod
    def to_model(note_entity: NoteEntity) -> "Note":
        data = note_entity.to_dict()
        note = Note(**data)
        return note
