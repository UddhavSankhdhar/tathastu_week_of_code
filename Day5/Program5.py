def sorting(List):
    odd = []
    eve = []
    for i in List:
        if i % 2 == 0:
            eve.append(i)
        else :
            odd.append(i)
    return sorted(odd, reverse = True) + sorted(eve)
size = int(input("Enter the number of elements in the array- "))
List = []
for i in range(size):
    List.append(int(input("Enter element number- " + str(i + 1) + " in the list- ")))
print("After sorting- ", str(sorting(List))[1:-1])
