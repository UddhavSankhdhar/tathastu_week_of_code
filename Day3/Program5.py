s1=int(input("Enter the no. of elements on list 1-"))
print("Enter the elements in list 1-")
l1=[]
for i in range(s1):
    l1.append(input())
s2=int(input("Enter the no. of elements on list 2-"))
print("Enter the elements in list 2-")
l2=[]
for i in range(s2):
    l2.append(input())
intersectionList= list(set(l1).intersection(set(l2)))
print("The intersection of list 1 and 2 -", ", ".join(intersectionList))
