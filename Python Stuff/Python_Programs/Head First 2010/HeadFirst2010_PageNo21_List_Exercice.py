'''
Use of recursion fucntion
'''

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

def print_lol(the_list):
    """ This function takes a positional argument called “the_list", which is any
    Python list (of, possibly, nested lists). Each data item in the provided list
    is (recursively) printed to the screen on its own line
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)        #calling a function from a function-recursive function
        else:
            print(each_item)
print_lol(movies)

