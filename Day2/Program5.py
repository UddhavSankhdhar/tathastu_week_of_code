n= int(input("Enter a number- "))
for i in range(n):
    print((str(n-i)+"*")*(n-1-i)+str(n-i))
for i in range(2,n+1):
    print((str(i)+"*")*(i-1)+str(i))

