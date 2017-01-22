import mido
import glob
from operator import attrgetter
from markov import markov_chainify, markov_dictify

list_of_chains = []

def dostuff(a):
    return a.channel

def get_files():
    list_of_midi_files = glob.glob('.\\_data\\midifiles\\clean_midi\\genres\\rock\\*.mid')
    #gives us list of absolute paths of files in rock genre
    return list_of_midi_files
def get_values(path):
    mid = mido.MidiFile(path)
    values = []
    #print(mid.length)
    #print(mid.type)
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track.name))
        for message in track:
            if not isinstance(message, mido.MetaMessage):
                values.append(message)

#    mid.close()
    delay = 0
    return values

def make_model(values):
    states = [([], 0)]
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
    #1print(vars(mido.Message))
def main():

    paths = get_files()
    #print(paths)
    midi_markov = []
    count=0
    for path in paths[1:11]:
        #print(path)
        print(count)
        values = get_values(path)
        midi_chains = make_model(values)
        midi_markov.extend(tuple(midi_chains))

        count+=1
        print(len(midi_markov))

    #cooldict = markov_dictify(midi_markov)
    #print()

main()
