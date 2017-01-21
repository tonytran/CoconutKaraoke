"""
In computer programming and software testing, smoke testing
(also confidence testing, sanity testing, build verification
test (BVT) and build acceptance test) is preliminary testing
to reveal simple failures severe enough to (for example) reject
a prospective software release.
~ https://en.wikipedia.org/wiki/Smoke_testing_(software)
"""
from unittest import TestCase


class ViewSmokeTestCase(TestCase):
    """
    Smoke tests to make sure that views load.
    """

    def setUp(self):
        from app import app
        self.app = app.test_client()

    def test_index(self):
        """
        Test that the index can be loaded.
        """
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

    def test_lyrics(self):
        """
        Test that the lyrics page can be loaded.
        """
        response = self.app.get('/lyrics')

        self.assertEqual(response.status_code, 200)

    def test_music(self):
        """
        Test that the music page can be loaded.
        """
        import app

        app.write_lyrics('test', 'This is a country song')
        app.write_lyrics('test', 'This is a country song')
        app.write_lyrics('test', 'This is a country song')
        app.write_lyrics('test', 'Sing sing sing sing.')

        app.S.push('test')

        response = self.app.get('/music')

        self.assertEqual(response.status_code, 200)
