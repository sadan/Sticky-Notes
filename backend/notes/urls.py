from django.conf.urls import url

from backend.notes.bindings import *

urlpatterns = [
    url(
        regex=r'^add/$',
        view=add_note,
        name='add_note'
    ),
    url(
        regex=r'^list/$',
        view=notes_list,
        name='notes_list'
    ),
    url(
        regex=r'^retrieve/(?P<note_id>[0-9]+)/$',
        view=retrieve_note,
        name='retrieve_note'
    ),
    url(
        regex=r'^destroy/(?P<note_id>[0-9]+)$',
        view=delete_note,
        name='delete_note'
    ),
    url(
        regex=r'^update/$',
        view=update_note,
        name='update_note'
    )
]
