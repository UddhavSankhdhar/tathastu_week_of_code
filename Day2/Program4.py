n= int(input("Enter the length of one side of diamond- "))
for i in range(n):
    print("* " * (n - i) + "    " * i + " *" * (n-i))
for i in range(2,n + 1):
    print("* " * i + "    " * (n - i) + " *" * i)
