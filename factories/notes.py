import factory

from backend.notes.models import Note


class NoteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Note

    text = factory.Sequence(lambda n: "Note Text %s" % n)
