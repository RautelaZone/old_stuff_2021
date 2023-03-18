'''
input = hello
output = l
'''

str = "rautelaraut"
dup=[]
for ch in str:
    if str.count(ch)>1:
        if ch not in dup:
            dup.append(ch)
print(dup)

'''
Using Dictionary
'''

str = "tutorialspoint"

duplicates = {}
for char in str:
      if char in duplicates:
          duplicates[char] += 1
      else:
          duplicates[char] = 1

for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")
