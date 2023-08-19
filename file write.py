# f = open("ahmadkarim.txt", "w")
# f.write("Ahmad is a good programmer")
# f.close()

# here I appand the file. Means ap jitni bar programme ko run karo gaay
#itni bar chalaygi
# f = open("file writing.txt", "a")
# f.write("Hi there! This is Ahmad karim here.\n")
# f.close()

# File handle read and write both.
f = open("file writing.txt", "r+")
print(f.read())
f.write("Welcome to the programming world")