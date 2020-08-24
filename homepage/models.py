from django.db import models
from django.utils import timezone


class PostModle(models.Model):
    body = models.CharField(max_length=280)
    post_time = models.DateTimeField(default=timezone.now)
    is_roast = models.BooleanField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
