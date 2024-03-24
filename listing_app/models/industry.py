from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=80, blank=False, null=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
