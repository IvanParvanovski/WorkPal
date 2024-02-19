from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class UserSuggestion(models.Model):
    """
    When someone wants to suggest a new possible value for the option fields, it should happen
    through that class.
    """
    field_name = models.CharField(max_length=100)
    suggestion = models.CharField(max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
