el=int(input("Enter the number of elements in the list- "))
print("Enter the elements- ")
List =[]
for i in range(el):
    List.append(input())
duplist=[]
for p in List:
    if p not in duplist:
        duplist.append(p)
print("List after removing the duplicates is- ",duplist)
