from django.db import models
from django.utils import timezone

from stickynotes.libs.managers import StickyNotesManager


class Note(models.Model):
    objects = StickyNotesManager()

    text = models.TextField()
    added_on = models.DateTimeField(default=timezone.now())
    last_updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
