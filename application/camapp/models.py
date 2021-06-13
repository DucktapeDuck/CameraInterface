import uuid

from django.db import models

# Create your models here.
class Instance(models.Model):
    """Model representing a book genre."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this instance')
    type = models.CharField(max_length=200, help_text='Enumeration of classes detected')
    time = models.DateTimeField(null=True)
    accuracy = models.FloatField(null=True, blank=True)
    image_location = models.CharField(max_length=200, blank=True, help_text='Location for stored image')

