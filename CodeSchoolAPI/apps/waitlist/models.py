from django.db import models

# Create your models here.

from django.db import models


class WaitlistEntry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email field',
                              max_length=100,
                              unique=True)
    LEVELS = (
        ('Entry', 'Entry'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior')
    )

    level = models.CharField(choices=LEVELS, verbose_name='Class Level',
                             max_length=50,default='Entry')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Waitlist Entrie'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
