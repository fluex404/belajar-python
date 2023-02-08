# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

filePath = '/Users/isasubani/Documents/belajar/python/belajar-python/Tutorial/asset/demofile2.txt'

f = open(filePath, 'a')
f.write(' update')
f.close()

f = open(filePath, 'r')
print(f.read())
f.close()

# filePath = '/Users/isasubani/Documents/belajar/python/belajar-python/Tutorial/asset/demofile3.txt'
# f = open(filePath, 'w') # after this the content have cleared
# print(f.read())

# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# f = open("myfile.txt", "x")
# f.close()

# f = open(filePath, 'x')  # u will got error because the file is exist

# you can try this if you file doesn't exist
# and automatily 
# f = open("myfile.txt", "w")