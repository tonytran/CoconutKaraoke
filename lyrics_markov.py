from __future__ import division
from collections import Counter
import glob


START = object()
END = object()


def markov_chainify(sentence, split_at=2):
    sentence = sentence.split()

    yield tuple([START] + sentence[:split_at - 1])

    if len(sentence) <= split_at:
        yield tuple(sentence)
    else:
        for sentence_offset in range(0, len(sentence) - split_at + 1):
            portion = []

            for split_offset in range(split_at):
                portion.append(sentence[sentence_offset + split_offset])

            yield tuple(portion)

    yield tuple(sentence[-split_at + 1:] + [END])


def markov_dictify(chain):
    decision_dict = dict()

    for portion in chain:
        decision_part = portion[:-1]
        next_part = portion[-1]

        if decision_part not in decision_dict:
            decision_dict[decision_part] = []

        decision_dict[decision_part].append(next_part)

    probability_dict = dict()

    for decision_part, next_parts in decision_dict.items():
        probability_dict[decision_part] = {}

        probabilities = Counter(next_parts)

        for part, count in probabilities.items():
            probability_dict[decision_part][part] = count / len(next_parts)

    return probability_dict


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

        line = ' '.join(reversed(line.split())).lower()

        line_chains = list(markov_chainify(line, split_at=3))

        song_chains.extend(line_chains)

    all_chains.extend(line_chains)

print(markov_dictify(all_chains))