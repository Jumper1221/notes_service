from django.urls import path
from .views import NoteListCreate, NoteRetrieveUpdateDestroy


urlpatterns = [
    path("notes", NoteListCreate.as_view(), name="note-list"),
    path("notes/<uuid:id>", NoteRetrieveUpdateDestroy.as_view(), name="note-detail"),
]
