from rest_framework_dataclasses.serializers import DataclassSerializer

from note.domain.entities import NoteEntity


class NoteEntitySerializer(DataclassSerializer):
    class Meta:
        dataclass = NoteEntity
