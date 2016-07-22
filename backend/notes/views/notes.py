from rest_framework import viewsets, status
from rest_framework.response import Response

from backend.notes.exceptions import *
from backend.notes.models import Note
from backend.notes.serializers.note import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        note = Note.objects.get_first(id=kwargs.get('note_id'))
        serializer = self.serializer_class(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        active_notes = self.queryset.filter(is_deleted=False)
        if active_notes.exists():
            serializer = self.serializer_class(active_notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise NotesDoesNotExist

    def update(self, request, *args, **kwargs):
        data = request.data

        note = Note.objects.get_first(id=data['id'])
        serializer = self.serializer_class(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        note = Note.objects.get_first(id=kwargs.get('note_id'))
        note.is_deleted = True
        note.save()
        raise SuccessfullyDeleted
