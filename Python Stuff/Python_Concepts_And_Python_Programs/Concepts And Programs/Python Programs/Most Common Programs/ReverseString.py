# without using any BIFs
str = "durga"
new = ""
i = len(str) - 1
while i >= 0:
    new = new + str[i]
    i = i - 1
print(new)

# Without Using BIFs
str = "durga"
new = ""
for ch in str:
    new = ch + new
print(new)

# With using Slicing
str = "durga"
print(str[::-1])

# With using BIF: reverse
str = "durga"
print("".join(reversed(str)))
