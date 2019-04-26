import midi
import os
import json

out = []
files_list = (os.listdir(os.getcwd()+"/data/midis"))
for file in files_list:
    out.append([])
    pattern = midi.read_midifile(os.getcwd()+"/data/midis/"+file)
    for part in pattern:
        for el in part:
            if el.name == "Note On":
                out[-1].append([])
                out[-1][-1].append(el.tick)
                out[-1][-1].append(el.pitch)
                out[-1][-1].append(el.velocity)
with open("data_from_midi.json", "w") as f:
    json.dump(out, f)

