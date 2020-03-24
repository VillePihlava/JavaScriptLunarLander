from django.db import models
from django.utils import timezone

class Score(models.Model):
    score = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)