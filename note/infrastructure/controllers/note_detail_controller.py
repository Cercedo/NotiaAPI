from dependency_injector.wiring import Provide
from rest_framework import generics

from note.application.services import (
    DeleteNoteService,
    GetNoteService,
    UpdateNoteService,
)
from note.domain.entities import NoteEntity
from note.infrastructure.configs import Container
from note.infrastructure.controllers.serializers import NoteEntitySerializer


class NoteDetailController(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteEntitySerializer
    get_note_service: GetNoteService = Provide[Container.get_note_service]
    update_note_service: UpdateNoteService = Provide[
        Container.update_note_service
    ]
    delete_note_service: DeleteNoteService = Provide[
        Container.delete_note_service
    ]

    def get_object(self) -> NoteEntity:
        return self.get_note_service.execute(id=self.kwargs["pk"])

    def perform_update(self, serializer: NoteEntitySerializer):
        data: NoteEntity = serializer.validated_data
        self.update_note_service.execute(
            id=self.kwargs["pk"], note_entity=data
        )

    def perform_destroy(self, instance: NoteEntity):
        self.delete_note_service.execute(id=instance.id)  # type: ignore
