write a function that looks for files with duplicate contents and flags them as the sample below:

def find_duplicates(rootpath)
-> [['a.txt', 'foo/c.txt'], ['b.txt', 'foo/bar/e.txt']]

the files live in a directory structure like this one:

root/
    a.txt -> "xyz"
    b.txt -> "1234"
    foo/
       c.txt -> "xyz"
       d.txt -> "abc"
       bar/
           e.txt -> "1234"