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
