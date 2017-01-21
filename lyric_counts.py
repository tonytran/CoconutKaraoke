from collections import defaultdict
import glob


songs_by_genre = defaultdict(list)


for file in glob.glob('_data/lyric_cache/*.txt'):
    with open(file) as file_handle:
        title = next(file_handle)
        artist = next(file_handle)
        genre = next(file_handle)

        #print(title, artist, genre)

        songs_by_genre[genre.lower().strip()].append(
            '%s - %s' % (artist.strip(), title.strip())
        )

for genre, songs in songs_by_genre.items():
    print('%s: %d' % (genre, len(songs)))