import os

try:
    man_file = open('C:/python3.8/Practice/man_file.txt', 'w+')
    man_file.write("All monologue from a man")
    other_file = open('C:/python3.8/Practice/other_file.txt', 'w+')
    other_file.write("All monologue from different man")

    man_file = open('C:/python3.8/Practice/man_file.txt')
    print(man_file.read())
    other_file = open('C:/python3.8/Practice/other_file.txt')
    print(other_file.read())


except IOError as err:
    print("File Error",err)

finally:
    if 'man_file' and 'other_file' in locals():
        man_file.close()
        other_file.close()

# os.remove("C:/python3.8/Practice/other_file.txt")
# os.remove("C:/python3.8/Practice/man_file.txt")