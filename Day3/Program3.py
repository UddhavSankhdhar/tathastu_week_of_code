st=input("Enter a string- ")
dupst=""
for i in st:
    if i not in dupst:
        dupst+=i
print("String without duplicates- ", dupst)
