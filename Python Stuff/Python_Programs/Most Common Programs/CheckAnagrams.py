
def anagram(s1, s2):
    if len(s1)==len(s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 == s2:
            print("Anagram")
        else:
            print("Not Anagram")
    else:
        print("Strings must be of equal length.")

s1 = "silent"
s2 = "listen"
anagram(s1, s2)