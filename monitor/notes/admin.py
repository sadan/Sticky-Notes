from django.contrib import admin

from backend.notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'added_on', 'last_updated_on', 'is_deleted')
    ordering = ('id',)


admin.site.register(Note, NoteAdmin)
