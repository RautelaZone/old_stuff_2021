no = int(input("How many terms? "))
# 0 1 1 2 3 5 8 13

n1,n2=0,1
count=0
if no < 0:
    print("Enter positive no: ")
elif no==1:
    print(n1,n2)
else:
    print("Fibonacci series is: ")
    while count<no:
        print(n1,end=" ")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1



