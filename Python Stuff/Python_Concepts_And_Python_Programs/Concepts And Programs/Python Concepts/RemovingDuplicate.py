'''
Solution to Exercise at Page No - 162
'''

lists = [12,15,1,52,15,32,95,52,95,15]

# changeToSet = set(lists)
# print(sorted(changeToSet))

removeD = []
for item in lists:
    if item not in removeD:
        removeD.append(item)
print(sorted(removeD))

# def sanitize(time_string):
#     if '-' in time_string:
#         splitter = '-'
#     elif ':' in time_string:
#         splitter = ':'
#     else:
#         return(time_string)
#     (mins, secs) = time_string.split(splitter)
#
#     return (mins + '.' +secs)
#
# with open('C:/python3.8/Practice/james.txt') as jaf:
#     data = jaf.readline()
# james = data.strip().split(',')
# with open('C:/python3.8/Practice/julie.txt') as juf:
#     data = juf.readline()
# julie = data.strip().split(',')
# with open('C:/python3.8/Practice/mikey.txt') as mif:
#     data = mif.readline()
# mikey = data.strip().split(',')
# with open('C:/python3.8/Practice/sarah.txt') as saf:
#     data = saf.readline()
# sarah = data.strip().split(',')
#
# james = sorted([sanitize(t) for t in james])
# julie = sorted([sanitize(t) for t in julie])
# mikey = sorted([sanitize(t) for t in mikey])
# sarah = sorted([sanitize(t) for t in sarah])
#
# unique_james=[]
# unique_julie=[]
# unique_mikey=[]
# unique_sarah=[]
#
# for each_t in james:
#     if each_t not in unique_james:
#         unique_james.append(each_t) #this will add list into unique_james if not in there or can say removing duplicacy
# print(unique_james[0:3])    #will give first three item from 0,1,2
#
# for each_t in julie:
#     if each_t not in unique_julie:
#         unique_julie.append(each_t) #this will add list into unique_julie if not in there or can say removing duplicacy
# print(unique_julie[0:3])    #will give first three item from 0,1,2
#
# for each_t in mikey:
#     if each_t not in unique_mikey:
#         unique_mikey.append(each_t) #this will add list into unique_mikey if not in there or can say removing duplicacy
# print(unique_mikey[0:3])    #will give first three item from 0,1,2
#
# for each_t in sarah:
#     if each_t not in unique_sarah:
#         unique_sarah.append(each_t) #this will add list into unique_sarah if not in there or can say removing duplicacy
# print(unique_sarah[0:3])    #will give first three item from 0,1,2


