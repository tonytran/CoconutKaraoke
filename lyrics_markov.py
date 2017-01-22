from markov import markov_chainify, markov_dictify, START, END
import glob
import random


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

state_map = markov_dictify(all_chains)

start_chains = [seq for seq in state_map.keys() if seq[0] == START]

line = list(random.choice(start_chains))

def weighted_choice_sub(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

while line[-1] != END:
    start_part = tuple(line[-2:])

    next_probabilities = state_map[start_part]

    weights = next_probabilities.values()

    winner = weighted_choice_sub(weights)

    next_part = list(next_probabilities.keys())[winner]

    line.append(next_part)

print(' '.join(reversed(line[1:-1])))