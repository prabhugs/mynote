from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.post_text

    post_text = models.CharField(max_length=500)
    published_date = models.DateTimeField('published on')

    def waspublishedrecently(self):
        return self.published_date >= timezone.datetime.now() - datetime.timedelta(days=1)

class Comment(models.Model):
    def __str__(self):
        return self.comment_text

    post = models.ForeignKey(Post)
    comment_text = models.CharField(max_length=500)
    commented_date = models.DateTimeField('commented on')