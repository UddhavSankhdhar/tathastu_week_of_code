n = int(input("Enter the length of one arm of pattern X- "))
for i in range(n):
    print(" "*i + "*" + " "*(n - 1 - i) + "*")
for i in range(n):
    print(" "*(n - 1 - i) + "*" + " "*i + "*")
