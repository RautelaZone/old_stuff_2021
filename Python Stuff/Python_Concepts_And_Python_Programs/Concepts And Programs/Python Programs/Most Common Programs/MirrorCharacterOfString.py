'''
Given a string and a number N, we need to mirror the characters from Nth position up to the length of the string
in the alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
Input : N = 3
        paradox
Output : paizwlc
'''

def compute(st,n):
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    answer=""
    for i in range(0,n):
        answer = answer+st[i]
    for i in range(n, len(st)):
        answer = answer + reverseAlphabet[ord(st[i]) - ord('a')]
    return answer

st = "paradox"
n = 4
answer = compute(st,n-1)
print("Word after Mirror image:",answer)

#using dictionary's and zip conecpt:
def mirrorChars(input,k):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dicChars=dict(zip(original,reverse))
    mirror=""
    start=input[0:k-1]
    end=input[k-1:]
    for i in range(0,len(end)):
        mirror = mirror+dicChars[end[i]]
    return start+mirror

input = 'paradox'
k = 3
answer = mirrorChars(st,n-1)
print("Word after Mirror image:",answer)
