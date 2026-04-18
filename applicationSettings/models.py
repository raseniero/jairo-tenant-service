import uuid
from django.db import models


class ApplicationSettings(models.Model):
    guid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)


    def __str__(self):
        return self.key