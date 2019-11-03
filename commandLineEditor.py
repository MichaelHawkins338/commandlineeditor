import time
import os.path
from os import path

filecheck = input("Enter a filename in current directory:")
print("Item exists:" + str(path.exists(filecheck)))

filename = input("Create new file with new name:")
file = open(filename + ".txt","w+")
filewrite = input("What would you like to save to this file?:")
file.write(filewrite)
file.close()
print("file and contents created and saved!")

fileread = input("Type a file name to display its content:")
if path.exists(fileread):
	print("File exists! Here are the contents...")
	file = open(fileread,"r")
	print(file.read())
	file.close()

print("closing in 5 seconds...")
time.sleep(5)