from markov import markov_chainify, markov_dictify
import glob


lyrics_dir = '_data/lyric_genre/rock/'

all_chains = []

for song_path in glob.glob(lyrics_dir + '*.txt'):
    with open(song_path) as song_handle:
        lines = song_handle.readlines()

        title = lines[0].strip()
        artist = lines[1].strip()
        genre = lines[2].lower().strip()

        lyrics = lines[4:]

    song_chains = []

    for line in lyrics:
        if not line.strip():
            continue

        line = list(reversed(line.lower().split()))

        line_chains = list(markov_chainify(line, split_at=3))

        song_chains.extend(line_chains)

    all_chains.extend(line_chains)

print(markov_dictify(all_chains))