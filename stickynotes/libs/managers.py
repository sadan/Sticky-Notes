from django.db import models


class StickyNotesManager(models.Manager):
    def get_first(self, **kwargs):
        # noinspection PyUnresolvedReferences
        queryset = self.model.objects.filter(**kwargs)
        if queryset.exists():
            return queryset.first()
