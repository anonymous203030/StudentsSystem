from django.db import models

from apps.users.models import User


class Certificate(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    UserCertificate = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserCertificate')
    created_at = models.DateTimeField(auto_now_add=True)