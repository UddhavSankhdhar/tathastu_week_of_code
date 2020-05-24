el = int(input("Enter the size of the tuple- "))
print("Enter the elements in tuple- ")
tp = []
for i in range(el):
    tp.append(input())
tp = tuple(tp)
element = input("Enter the element whose number of occurrences you want to know- ")
print("Number of occurences- ",tp.count(element))
