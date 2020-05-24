s = int(input("Enter the number of terms you want to add in the Dictonary- "))
dicty = dict()
for i in range(s):
    key = input("Enter the key for " + str(i + 1) + " in dictonary- ")
    val = int(input("Enter the value for " + str(i + 1) + " in dictonary- "))
    dicty[key] = val
res = dict()
for key,val in dicty.items():
    if val not in res.values():
        res[key] = val
print("Removed duplicate values- ", res)
