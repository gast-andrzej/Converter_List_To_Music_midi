import mido

g = list((__import__('random').randint(1,127), __import__('random').randint(30, 120)) for i in range(200))

# example_list = [(Sound note ,Time note),(next note like before)]                [(127,50),(50,90)]

def Convix(program_music_int, list_track):
    # 127 in list track is MAX
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    track.append(mido.Message('program_change', program=program_music_int, time=0))
    for i in list_track:
        z = int(i[1])*1000    # Time in seconds
        x = int(i[0])         # Sound
        track.append(mido.Message('note_on', note=x, velocity=127, time=z))    # change volume, change velocity
    mid.save('new_song.mid')


# Convix(0,g)
# Convix(0,[(127,1), (50, 1), (80,1), (127,1), (50, 1), (80,1), (127,1), (50, 1), (80,1), (127,1), (50, 1), (80,1)])


def ConvixWithVelocity(program_music_int,list_track):
    # 127 in list track is MAX
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    track.append(mido.Message('program_change', program=program_music_int, time=0))
    for i in list_track:
        z = int(i[1])*1000    # Time in seconds
        y = int(i[2])
        x = int(i[0])         # Sound
        track.append(mido.Message('note_on', note=x, velocity=y, time=z))    # change volume, change velocity
    mid.save('new_song.mid')

# ConvixWithVelocity(Your program,[(Your_note, Time_your_note_in_seconds, Volume_max_127), (Your_next_note, Time_your_note_in_seconds, Volume_max_127)])
# ConvixWithVelocity(0,[(127,6,127), (50, 2,127), (80,2,100), (127,6,100), (50, 2,100), (80,2,127),(127,6,127), (50, 2,127), (80,2,100), (127,6,100), (50, 2,100), (80,2,127),(127,6,127), (50, 2,127), (80,2,100), (127,6,100), (50, 2,100), (80,2,127),(127,6,127), (50, 2,127), (80,2,100), (127,6,100), (50, 2,100), (80,2,127)])

# program 0 like a piano