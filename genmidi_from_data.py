import midi
import json

with open("out_gen.json") as f:
    data = json.loads(f.read())

pattern = midi.Pattern()
track = midi.Track()
pattern.append(track)

for block in data:
    print(block)
    on = midi.NoteOnEvent(tick=block[0], data=[block[1],block[2]])
    track.append(on)
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
midi.write_midifile("gen.mid", pattern)


