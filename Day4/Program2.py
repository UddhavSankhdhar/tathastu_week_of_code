sizeL = int(input("Enter the number of tuples- "))
sizeT = int(input("Enter the number of elements you want in each tuple- "))
List = []
for i in range(sizeL):
    print("Enter the elements in the Tuple- ", i + 1)
    Tuple = []
    for p in range(sizeT):
        Tuple.append(int(input("Enter the element " + str(p + 1) + "- ")))
    List.append(tuple(Tuple))
Ind = int(input("Enter the index to sort the list- "))
List.sort(key=lambda x: x[Ind])
print("Sorted tuple List- ",List)
