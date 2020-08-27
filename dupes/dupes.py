import os
import filecmp

texts = []
output = []

for root, _, files in os.walk("./root", topdown=True):
    for f in files:
        texts.append(root + "/" + f)

for i, t in enumerate(texts):
    for j, z in enumerate(texts):
        if i < j:
            if filecmp.cmp(t, z):
                output.append([t, z])

for o in output:
    print(o)
