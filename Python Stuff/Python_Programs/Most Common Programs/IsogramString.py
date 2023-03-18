'''
Isogram String is initial 2 words+last 2 words
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''

# str="AnilRautela"
# start= str[0:2]
# end= str[-2:]
# print(start,end)

class A:
    def method(self,str):
        if len(str)>1:
            new = str[0:2]+str[-2:]
            print(new)
        else:
            return print("Empty")
str="w3school"
obj=A()
obj.method(str)

