from django.conf.urls import url

from backend.notes.bindings import *

urlpatterns = [
    url(
        regex=r'^add/$',
        view=add_note,
        name='add_note'
    )
]
