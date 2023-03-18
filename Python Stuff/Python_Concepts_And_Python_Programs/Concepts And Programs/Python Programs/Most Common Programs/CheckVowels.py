
#using list comprehension
str = "Geeks for Geeks"
vowels="aeiou"

str.swapcase()
final=[item for item in str if item in vowels]
print(len(final))
print(final)

#Using Dictionary
str="Geeks for Geeks"
vowels="aeiou"

count={}.fromkeys(vowels,0)
str.swapcase()
for item in str:
    if item in vowels:
        count[item]+=1
print(count)