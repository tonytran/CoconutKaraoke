from unittest import TestCase
from app import open_file
from app import rand_song_title
from app import return_lyrics



class TestOpen_file(TestCase):

    def test_open_file_true(self):
        genre = "pop"
        self.assertTrue(open_file(genre))

    def test_open_file_false(self):
        genre = "wrong"
        with self.assertRaises(TypeError):
            open_file(genre)


class TestRand_song_title(TestCase):

    def test_rand_song_title_true(self):
        self.assertTrue(rand_song_title())


class TestReturn_lyrics(TestCase):

    def test_return_lyrics_true(self):
        genre = "pop"
        self.assertTrue(return_lyrics(genre))

    def test_return_lyrics_false(self):
        genre = "wrong"
        with self.assertRaises(TypeError):
            return_lyrics(genre)


class TestObject_Retrievals(TestCase):

    def setUp(self):
        from app import app
        self.app = app.test_client()

    def test_object_retrievals(self):
        with self.app.session_transaction() as sess:
            sess['genre'] = 'pop'
            response = self.app.get('/music')
        self.assertEqual(302, response.status_code)


