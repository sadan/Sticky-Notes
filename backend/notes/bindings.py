from backend.notes.views.notes import NotesViewSet

add_note = NotesViewSet.as_view({
    'post': 'create'
})

