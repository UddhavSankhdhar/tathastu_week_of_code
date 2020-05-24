s = int(input("Enter the number of terms in the dictonary- "))
dicty = dict()
for i in range(s):
    key = input("Enter the key for item " + str(i + 1) + " in dictonary- ")
    val = int(input("Enter the value for item " + str(i + 1) + " in dictonary- "))
    dicty[key] = val

print("The second largest term in the dictonary is- ", list(sorted(dicty.values()))[-2])
