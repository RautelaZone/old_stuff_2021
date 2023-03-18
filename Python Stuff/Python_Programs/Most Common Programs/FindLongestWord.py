'''
Find Longest Word
key= key is the function used to measure the size of the elements of your list
'''
def find_longest_word(word):
    longest_word =  max(word, key=len)
    print("Longest word is:",longest_word,"with length", len(longest_word))

word="be confident and be yourself"
find_longest_word(word.split(" "))