import numpy as np
from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import json
import save_load_model

with open("data_from_midi.json") as f:
    data = json.loads(f.read())

size = 20
y = []
d = []
songs = 10
n = 0
for song in data:
    x = []
    n+=1
    if n>songs:
        break
    for i in range(len(song)-size):
        x.append(song[i:size+i].copy())
        y.append(song[size+i])
    for el in x:
        d.append([])
        for ell in el:
            d[-1].append(ell[0])
            d[-1].append(ell[1])
            d[-1].append(ell[2])

y = np.asarray(y, dtype=np.uint32)
d = np.asarray(d, dtype=np.uint32)
print(d.shape)
print(y.shape)


model = Sequential()
model.add(Dense(60, activation="relu", input_shape=(60,)))
model.add(Dense(100, activation="relu"))
model.add(Dense(3))
model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.fit(d, y, epochs=50, batch_size=20, verbose=1)

save_load_model.save_model_json(model, "model_v1.json")
save_load_model.save_weights_h5(model, "weights_v1.h5")

s = d[0]
pred = model.predict(np.asarray([d[0]]))
pred = np.asarray(pred, dtype=np.int32)

if pred[0][0] < 0:
    pred[0][0] = 0
if pred[0][1] < 0:
    pred[0][1] = 0
if pred[0][2] < 0:
    pred[0][2] = 0

out = []

for i in range(1000):
    s = np.append(s, pred[0])
    pred = model.predict(np.asarray([s[-size*3:]]))
    pred = np.asarray(pred, dtype=np.int32)
    if pred[0][0] < 0:
        pred[0][0] = 0
    if pred[0][1] < 0:
        pred[0][1] = 0
    if pred[0][2] < 0:
        pred[0][2] = 0
    print(pred)
    out.append(pred.tolist()[0])

print(len(out))

with open("out_gen.json", "w") as f:
    json.dump(out, f)


