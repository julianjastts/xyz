import os
import filecmp

texts = []
output = []

for root, dirs, files in os.walk("./root", topdown=True):
    for f in files: 
        n = root+"/"+f
        texts.append((f,n))

for i,t in enumerate(texts): 
    for j,z in enumerate(texts): 
        if i < j:
            if filecmp.cmp(t[1],z[1]):
                output.append([t[1],z[1]])
                
for o in output:
    print(o)