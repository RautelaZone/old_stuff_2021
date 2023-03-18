'''
read(): will read all data of a file
readline(): reads line by line
readlines(): reads everything from a file including special character or next line \n
seek() : used to change the position of the File Handle to a given specific position.
0: sets the reference point at the beginning of the file
1: sets the reference point at the current file position
2: sets the reference point at the end of the file
'''
file1 = open("C:/Users/anilr/Desktop/Inn-Flow Work Data/2021/March/10March_DOT/readfile.txt", "r+")
print("Output of Read function is:")
print(file1.read()) #will read all data of a file
print("*"*50)

file1.seek(0) #used to change the position of the File Handle to a given specific position.

print("Output of Readline function is ")
print(file1.readline()) #read line by line
print("*"*50)

file1.seek(0)

print("Output of Read(9) function is ")
print(file1.read(9)) #read first to 8th character, 9th will be skipped
print("*"*50)

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9)) #read line by line till 8th character
print("*"*50)

file1.seek(0)

print("Output of Readlines function is ")
print(file1.readlines()) #read everything from a file including special character or next line \n
print("*"*50)
file1.close()