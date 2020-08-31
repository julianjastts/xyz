#!/usr/bin/python3

import filecmp, os, pathlib, hashlib

def getFilePaths(dir):
    hasher = hashlib.md5()
    for path, subdirs, files in os.walk(dir):
        for name in files:
            buf = ''
            filePath=pathlib.PurePath(path, name)
            with open(filePath,'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
                print('path={}'.format(filePath))
                print('buf={}'.format(buf))
                print(hasher.hexdigest())


getFilePaths("root")
