file = open("session11.py", "r")
data = file.read(1)
print(data)
print("==============")
data = file.read(5)
print(data)

"""print("==============")
data = file.read()
print(data)
"""
print("is file closed: ", file.closed)
file.close()# explicitly closing file

print("Is file closed: ", file.closed)