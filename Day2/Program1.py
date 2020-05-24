n=int(input("Enter a Number :"));
if(n%2==0):
    print(n, "is a even number")
else:
    print(n, "is a odd number")
if n > 1:

    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")

else:
    print(n, "is not a prime number")
p=n
temp=p
rev=0
while(p>0):
    dig=p%10
    rev=rev*10+dig
    p=p//10
if(temp==rev):
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")

sum = 0

# find the sum of the cube of each digit
temp = n
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
