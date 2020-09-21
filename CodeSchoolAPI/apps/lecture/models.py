from django.db import models

from apps.users.models import User


class Lecture(models.Model):
    title =  models.CharField(max_length=50)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='',
                                     blank=True)
    date = models.DateField()
    duration = models.IntegerField(help_text='Enter number of hours')
    slides_url = models.CharField(max_length=255)
    is_required = models.BooleanField(default=True)
    is_subscribed = models.ManyToManyField(User,through='Subscription')


class Subscription(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True )
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    reacted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Owner:{self.user}, Lecture: {self.lecture}, Rating: {self.rating}'