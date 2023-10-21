from typing import List

from dependency_injector.wiring import Provide
from rest_framework import generics

from note.application.services import CreateNoteService, ListNoteService
from note.domain.entities import NoteEntity
from note.infrastructure.configs import Container
from note.infrastructure.controllers.serializers import NoteEntitySerializer


class NoteListController(generics.ListCreateAPIView):
    serializer_class = NoteEntitySerializer
    list_note_service: ListNoteService = Provide[Container.list_note_service]
    create_note_service: CreateNoteService = Provide[
        Container.create_note_service
    ]

    def get_queryset(self) -> List[NoteEntity]:
        return self.list_note_service.execute()

    def perform_create(self, serializer: NoteEntitySerializer) -> None:
        data: NoteEntity = serializer.validated_data
        self.create_note_service.execute(data)
