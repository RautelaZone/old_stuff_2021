name = "appda"
rev=""

for i in name:
    rev= i+rev
# print(rev)
if rev==name:
    print("Palindrome")
else:
    print("Not Palindrome")

#another method
def isPalindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

s = "malayalam"
ans = isPalindrome(s)
if (ans):
    print("Palindrome")
else:
    print("Not Palindrome")