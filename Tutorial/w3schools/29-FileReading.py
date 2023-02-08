
filePath = '/Users/isasubani/Documents/belajar/python/belajar-python/Tutorial/asset/demofile.txt'
f = open(filePath, 'r')
print(f.read())

f = open(filePath, 'r')
print(f.readline(), f.readline())

f = open(filePath, 'r')
for x in f: 
    print(x)


f.close()