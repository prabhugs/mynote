from django.test import TestCase

import datetime
from django.utils import timezone
from notes.models import Post

# Create your tests here.

class PostMethodTests(TestCase):
    def test_waspublishedrecently_with_future_post(self):
        """
        :return: False for post whose published_date is in the future
        """
        time = timezone.datetime.now() + datetime.timedelta(days=30)
        future_post = Post(published_date = time)
        self.assertEqual(future_post.waspublishedrecently(), False)

    def test_waspublishedrecently_with_old_post(self):
        """
        :return: False for post whose published_date is greater than 24hrs from now
        """
        time = timezone.datetime.now() - datetime.timedelta(days=30)
        future_post = Post(published_date = time)
        self.assertEqual(future_post.waspublishedrecently(), False)

    def test_waspublishedrecently_with_recent_post(self):
        """
        :return: True for post whose published_date is not less than 24hrs from now
        """
        time = timezone.datetime.now() - datetime.timedelta(hours=1)
        future_post = Post(published_date = time)
        self.assertEqual(future_post.waspublishedrecently(), True)