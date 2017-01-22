import mido
from operator import attrgetter

def dostuff(a):
    return a.channel


def main():

    mid = mido.MidiFile('.\_data\midifiles\clean_midi\genres\pop\\(Sexual) Healing.mid')
    values = []
    print(mid.length)
    print(mid.type)
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for message in track:
            if not isinstance(message, mido.MetaMessage):
                values.append(message)


    delay = 0
    return values

def make_model(values):
    states = [([], 0)]
    curr = []
    for message in values:
        if message.type == 'note_off' or message.type =='note_on':
            if message.type == 'note_off':
                print(curr)
                #print('removing')
                curr.remove(message.note)
            else:
                print('adding')
                #print(curr)
                curr.append(message.note)
            states.append((curr.copy(),message.time))

    #print(states)


    copylist = []
    for state in states:
        if state[1] == 0 and len(copylist) > 0:
            a = copylist.pop()
            b = state
            new_state = (b[0], a[1])
            copylist.append(new_state)

        else:
            copylist.append(state)
    print(copylist)
    #1print(vars(mido.Message))
