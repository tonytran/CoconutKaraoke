import random
import glob
from mido import MidiFile, MidiTrack, Message, MetaMessage
from markov import START, END, markov_chainify, markov_dictify

def weighted_choice_sub(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i




def make_model(values):
    states = [((), 0)]
    curr = []
    for message in values:
        if message.type == 'note_off' or message.type =='note_on':
            if message.type == 'note_off':
                #print(curr)
                #print('removing')
                if message.note in curr:
                    curr.remove(message.note)
            else:
                #print('adding')
                #print(curr)
                curr.append(message.note)
            states.append((tuple(curr.copy()),message.time))

    #print(states)


    copylist = []
    for state in states:
        if state[1] == 0 and len(copylist) > 0:
            a = copylist.pop()
            b = state
            new_state = (tuple(b[0]), a[1])
            copylist.append(tuple(new_state))

        else:
            copylist.append(tuple(state))
    #Sprint(copylist)
    chains =  markov_chainify(copylist)

    return (tuple(chains))


def main():
    MAX_SONG_LEN = 60
    genre_dir = '_data/midifiles/clean_midi/genres/rock/'
    all_chains = []
    for song_path in glob.glob(".\\_data\\midifiles\\clean_midi\\genres\\rock\\*.mid")[1:10]:
        print(song_path)
        mid = MidiFile(song_path)
        values = []
        for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track.name))
            for message in track:
                if not isinstance(message, MetaMessage):
                    values.append(message)
        chain = make_model(values)
        all_chains.extend(chain)

    state_map = markov_dictify(all_chains)

    segments = [START]


    while segments[-1] != END:#taking the last part found and pulling the prob out of state map
        start_part = tuple(segments[-1:])

        next_probabilities = state_map[start_part]
        weights = next_probabilities.values()
        winner = weighted_choice_sub(weights)
        next_part = list(next_probabilities.keys())[winner]
        segments.append(next_part)
    mid = MidiFile()
    track = MidiTrack()
    curr = []
    last_delay = 0
    mid.tracks.append(track)
    ticks = 0
    in_use = []
    is_in_use = {}
    for i in range(len(segments)):
        if isinstance(segments[i],tuple): #START and END are objects and I can't index/key through them
        #getting mem error for some reason
        #I wanted to see what the song would look like without me attempting to detect changes
            segment = segments[i]

            note_list = segment[0]
            for note in note_list:
                #generate a message and turn on
                track.append(Message('turn_on', note = note, time = segment[1]))


                curr = note_list
                #if we do this all the time how can i move to the next item and call a diff on it?
                #use segments of -1? no thats not it i-1? 


            ticks+=segment[1]






        if ticks > MAX_SONG_LEN:
            break
    mid.save('some.mid')
main()
