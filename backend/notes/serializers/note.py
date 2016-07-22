from rest_framework.serializers import ModelSerializer

from backend.notes.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'text', 'added_on', 'last_updated_on', 'is_deleted')
        read_only_fields = ('id', 'added_on', 'last_updated_on')
