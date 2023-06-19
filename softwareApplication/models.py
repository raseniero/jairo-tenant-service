import uuid
from django.db import models


class Software(models.Model):
    guid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    applicationCategory = models.CharField(max_length=50, blank=True)
    applicationSubCategory = models.CharField(max_length=50, blank=True)
    applicationSuite = models.CharField(max_length=50, blank=True)
    softwareVersion = models.CharField(max_length=50, blank=True)
    
    
 

    def __str__(self):
        return self.name