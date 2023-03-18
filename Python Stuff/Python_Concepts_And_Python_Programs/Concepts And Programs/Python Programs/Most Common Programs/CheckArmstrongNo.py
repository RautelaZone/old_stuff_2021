'''
Find whether Armstrong or Not
For ex: 153
1*1*1+5*5*5+3*3*3 should be equal to no i.e; 153
so 153 is Armstrong No.
12 !=1*1+2*2 so Not an Armstrong No.

First program is my thought and second one is copied
'''

num=int(input("Enter a number: "))
strNum=str(num)
sum=0
order=len(str(num))

for i in range(len(strNum)):
    # r=int(strNum[i])*int(strNum[i])*int(strNum[i])
    r = int(strNum[i]) ** order  # **3 means no is to the power 3 or no^3
    sum += r

if sum==num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")

print("*"*50)

num = int(input("Enter a number: "))
sum = 0
temp = num
order=len(str(num))
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

