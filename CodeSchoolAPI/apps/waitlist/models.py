from django.db import models

# Create your models here.

from django.db import models

from apps.utils.models import Time
# from apps.users.models import User


class WaitlistEntry(Time,models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email field',
                              max_length=100,
                              unique=True)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Waitlist Entrie'