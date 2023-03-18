oriNo=int(input("Enter a number:"))
no=oriNo
reverse = 0

while no>0:
    rem=no%10
    reverse=(reverse*10)+rem
    no=no//10
print(f"Reverse of {oriNo} is:", reverse)
