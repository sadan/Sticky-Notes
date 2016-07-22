from backend.notes.views.notes import NotesViewSet

add_note = NotesViewSet.as_view({
    'post': 'create'
})

notes_list = NotesViewSet.as_view({
    'get': 'list'
})

retrieve_note = NotesViewSet.as_view({
    'get': 'retrieve'
})

update_note = NotesViewSet.as_view({
    'put': 'update'
})

delete_note = NotesViewSet.as_view({
    'delete': 'destroy'
})
