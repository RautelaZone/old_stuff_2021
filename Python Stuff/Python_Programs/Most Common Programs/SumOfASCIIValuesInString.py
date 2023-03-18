s = "I am a geek"
s = s.split(" ")

sum = 0
for item in s:
    for i in item:
        sum = sum+ord(i)
print(sum)

