from django.db import models

from apps.utils.models import Time
from apps.users.models import User


class Certificate(Time,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    UserCertificate = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserCertificate')
