## how to give a path
file = open("session11.py", "r")
#file = open("/Users/ishantKumar/downloads/session11.py", "r")

print(type(file))

fileContents = file.read()
print(type(fileContents))

print(fileContents)
print(len(fileContents))

#Re-Read in file
fileContents = file.read() #Re- Read
print(fileContents)

#Once a file is open and read, we cannot re-read it
#

