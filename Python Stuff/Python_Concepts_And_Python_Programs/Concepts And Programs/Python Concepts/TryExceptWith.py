import os

try:
    with open('C:/python3.8/Practice/man_file.txt', 'w+') as man_file:
        man_file.write("All monologue from a man")
    with open('C:/python3.8/Practice/other_file.txt', 'w+') as other_file:
        other_file.write("All monologue from different man")

    with open('C:/python3.8/Practice/man_file.txt') as man_file:
        print(man_file.read())
    with open('C:/python3.8/Practice/other_file.txt') as other_file:
        print(other_file.read())

except IOError as err:
    print("File Error",err)

os.remove("C:/python3.8/Practice/other_file.txt") #will remove the file
os.remove("C:/python3.8/Practice/man_file.txt") #will remove the file