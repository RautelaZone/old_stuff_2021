'''
write() : Inserts the single string in a single line in the text file
writelines() : Used to insert multiple strings at a single time
'''
file1 = open('C:/Users/anilr/Desktop/Inn-Flow Work Data/2021/March/10March_DOT/appendfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("C:/Users/anilr/Desktop/Inn-Flow Work Data/2021/March/10March_DOT/appendfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("C:/Users/anilr/Desktop/Inn-Flow Work Data/2021/March/10March_DOT/appendfile.txt", "r")
print("Output of Read after appending")
print(file1.read())
print("*"*50)
file1.close()

# Write-Overwrites
file1 = open("C:/Users/anilr/Desktop/Inn-Flow Work Data/2021/March/10March_DOT/appendfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("C:/Users/anilr/Desktop/Inn-Flow Work Data/2021/March/10March_DOT/appendfile.txt", "r")
print("Output of Read after writing")
print(file1.read())
print("*"*50)
file1.close()