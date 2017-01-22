from mido import MidiFile, MidiTrack, Message, MetaMessage
from markov import START, END
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)
lists = [([32,65,37],0), ([65, 37], 3), ([65, 48], 3), ([65], 56), ([42,17,61],54), ([47,2,13],149), ([143,44, 44,42,11,30],2000),
 ([44,55,11,44,254],4000), ([101,200,134], 600),([45,11,43],3), ([],3),([65, 37], 3),([],3),([65, 37], 3),([],3),([65, 37], 3),([32,65,37],0), ([65, 37], 3), ([65, 48], 3)]


curr_state = []
for tup in lists:
    print(tup)
    note_list = tup[0]
    if len(curr_state) == 0:
        for note in note_list:
            track.append(Message('note_on', note = note, time = tup[1]))
            curr_state = note_list
    else:
        if curr_state != note_list:
            items = set(curr_state) - set(note_list)
            for item in items:
                track.append(Message('note_off', note = note, time = tup[1]))

#track.append(Message('note_off', note=37, velocity= 100, time = 45))

mid.save('new_song.mid')
