from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.posttext

    posttext = models.CharField(max_length=500)
    publisheddate = models.DateTimeField('date published')

    def waspublishedrecently(self):
        return self.publisheddate >= timezone.datetime.now() - datetime.timedelta(days=1)