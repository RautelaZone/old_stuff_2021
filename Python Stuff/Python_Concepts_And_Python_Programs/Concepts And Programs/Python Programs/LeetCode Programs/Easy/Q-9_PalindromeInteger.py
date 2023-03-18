def isPalin(no):
    reverse = 0
    if no < 0:
        return False
    else:
        while no > 0:
            rem = no % 10
            reverse = (reverse * 10) + rem
            no = no // 10
        if reverse == temp:
            return True
        else:
            return False

no = int(input("Enter a number:"))
temp=no
print(isPalin(no))
