from datetime import datetime

from django.db import models

from apps.users.models import User

from apps.lecture.models import Lecture
from django.utils import timezone


class Comment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.ManyToManyField(User, through='CommentRelationship',
                                      related_name='liked')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lecture:{self.lecture}, Commented By:{self.owner}'

class CommentRelationship(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL,
                                null=True)
    comment = models.OneToOneField(Comment , on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    liked_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'Liked By{self.user}'
