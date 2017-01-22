import glob
import os
import os.path


cache_dir = '_data/lyric_cache'
genre_dir = '_data/lyric_genre'

for song_file in glob.glob(cache_dir + '/*.txt'):
    with open(song_file) as file_handle:
        lines = file_handle.readlines()

        title = lines[0].strip()
        artist = lines[1].strip()
        genre = lines[2].lower().strip()

        lyrics = lines[4:]

    if genre == 'hip hop/rap':
        genre = 'rap'
    elif genre == 'r&b;':
        genre = 'rb'

    if not os.path.exists(genre_dir + '/' + genre):
        os.mkdir(genre_dir + '/' + genre)

    os.rename(
        song_file,
        '%s/%s/%s' % (
            genre_dir,
            genre,
            os.path.basename(song_file),
        )
    )