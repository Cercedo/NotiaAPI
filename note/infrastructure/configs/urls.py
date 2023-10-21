from django.urls import path

from note.infrastructure.controllers import (
    NoteDetailController,
    NoteListController,
)

urlpatterns = [
    path("note/", NoteListController.as_view()),
    path("note/<int:pk>/", NoteDetailController.as_view()),
]
