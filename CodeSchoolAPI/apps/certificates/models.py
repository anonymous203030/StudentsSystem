from django.db import models

from apps.utils.models import Time

class Certificate(Time,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
