'''
Location of module is: C:\Users\anilr\Desktop\Practice\Modules\nester
'''

import nester #also can be used as from nester import print_lol

cast=['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.print_lol(cast) #function inside a module can be called by its namespace

print("*"*50)

# another way to perform this:
from nester import print_lol

cast=['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
print_lol(cast)

