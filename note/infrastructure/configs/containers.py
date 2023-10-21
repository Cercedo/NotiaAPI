from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)
from dependency_injector.providers import Aggregate, Factory

from note.application.services import (
    CreateNoteService,
    DeleteNoteService,
    GetNoteService,
    ListNoteService,
    UpdateNoteService,
)
from note.infrastructure import controllers
from note.infrastructure.orms.repositories import PostgresNoteRepository


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(modules=[controllers])

    note_repository = Aggregate(
        postgres=Factory(PostgresNoteRepository),
    )
    list_note_service = Factory(
        ListNoteService, note_repository=note_repository.postgres()
    )
    create_note_service = Factory(
        CreateNoteService, note_repository=note_repository.postgres()
    )
    get_note_service = Factory(
        GetNoteService, note_repository=note_repository.postgres()
    )
    update_note_service = Factory(
        UpdateNoteService, note_repository=note_repository.postgres()
    )
    delete_note_service = Factory(
        DeleteNoteService, note_repository=note_repository.postgres()
    )
