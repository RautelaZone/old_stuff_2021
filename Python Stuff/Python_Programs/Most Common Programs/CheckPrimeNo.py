
class Solution:
    def checkPrime(self,no):

        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
        return flag


num = int(input("Enter a number: "))
obj=Solution()
obj.checkPrime(num)

flag = False
if flag:
    print (num, "is not a prime number")
else:
    print (num, "is a prime number")




