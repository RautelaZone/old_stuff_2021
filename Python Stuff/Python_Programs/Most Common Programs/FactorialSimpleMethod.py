'''
Done by following two methods
for i in range(no,0,-1):
for i in range(1,no + 1):
'''
no=int(input("Enter a no: "))
result=1
if no in [0, 1]:
    print(no,"! is: 1")
else:
    for i in range(no,0,-1):
        result=result*i
    print(no,"! is:", result)

print("*"*50)

no=int(input("Enter a no: "))
result=1
if no ==0:
    print(no,"! is: 1")
else:
    for i in range(1,no + 1):
        result=result*i
    print(no,"! is:", result)