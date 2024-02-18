# models in this folder will not be migrated because the app
# is not installed in the settings apps
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class UserSuggestionAbstract(models.Model):
    """
    When someone wants to suggest a new possible value for the option fields, it should happen
    through that class.
    """
    field_name = models.CharField(max_length=100)
    suggestion = models.CharField(max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class IdentifiersAbstract(models.Model):
    """
    Provides an interface for contacts. The type can be any sort of social media or address.
    For example, type can be 'email' and value can be 'example@example.com'
    """
    type = models.CharField(max_length=40)
    value = models.CharField(max_length=96)

    class Meta:
        abstract = True
