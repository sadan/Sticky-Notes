from django.core import management

from factories.notes import NoteFactory


class Command(management.BaseCommand):
    def header(self, title):
        self.stdout.write('========================================================')
        self.stdout.write('-----%s-----' % title)

    def handle(self, *args, **options):
        self.header("Deleting database")
        management.call_command('flush', interactive=False, verbosity=0)

        self.header("Adding 5 Notes")
        NoteFactory.create_batch(size=5)
