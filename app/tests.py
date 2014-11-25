from django.test import TestCase

from .models import Album


class TheTest(TestCase):
    def test_this(self):
        a = Album.objects.create(title='Album Title')
        a.tracks.update_or_create({'title': 'Track 1'}, {})
        self.assertEqual(1, 1)
