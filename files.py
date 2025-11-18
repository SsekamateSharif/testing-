import os
# file handling using python 
# follows RAWXD 
# Reading 
f = open("names.txt", "r")
# reading all the text in the file 
# print(f.read())
# close the file  
# reading line by line 
for line in f:
    print(line)
f.close()

# Appending to a file 
f = open("names.txt", "a")
f.write("\nNail")
f.close()

f = open("names.txt", "r")
for line in f:
    print(line)
f.close()

# Writing or overwriting a file 
f = open("children.txt", "w")
f.write(" ")
f.close()

#Creating files 
# not considering if they exist 

f = open("clients.txt", "w")
f.close()

#considering if the file exists 
if not os.path.exists("Dave.txt"):
    f = open("Dave.txt", "x")
    f.close()
else:
    print("File already exists")

# deleting files; we delete files that already are in existance 

if os.path.exists("Dave.txt"):
    os.remove("Dave.txt")
    f.close()
else:
    print("The file doesnot exist")

# appending text to the childrens text file 
f = open("children.txt", "a")
f.write("Latif")
f.write("\nKelly")
f.write("\nIbrahim")
f.close()

f = open("children.txt", "a")
f.write("\nKevina")
f.write("\nDaniel")
f.write("\nWirtz")
f.close()

# reading the data in the file children 
f = open("children.txt", "r")

for line in f:
    print(line)
f.close()