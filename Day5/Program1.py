def rep_0_by_5(num):
    return int(str(num).replace('0','5'))
num = int(input("Enter a number- "))
print("Replacing 0 with 5- ", rep_0_by_5(num))
