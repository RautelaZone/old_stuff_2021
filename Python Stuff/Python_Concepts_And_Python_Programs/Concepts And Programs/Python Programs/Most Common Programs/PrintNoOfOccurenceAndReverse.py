"""
Write a program to print the number of occurrences of each letter in a string and
then build a string the string with unique characters in reverse order.
"""

str = "ApPle"

str = str.lower()
d = {}
for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in str:
    if d[i] != 0:
        print("{}{}".format(i, d[i]), end=" ")
        d[i] = 0
print()
s = list(str)
final_list = ""
for num in s:
    if num not in final_list:
        final_list+=num
print(final_list[::-1])
