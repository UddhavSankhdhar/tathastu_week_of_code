def KS(w, List):
    if w == 0 or len(List) == 0:
        return 0
    if len(List) == 1:
        if List[0][0] > w:
            return 0
        return List[0][1]
    if List[0][0] > w:
        return KS((w, List[1:]))
    return max(List[0][1] + KS(w - List[0][0], List[1:]), KS(w, List[1:]))
s =  int(input("Enter the number of items- "))
List = []
for i in range(s):
    w = int(input("Enter the w for item number- " + str(i + 1) + "- "))
    val = int(input("Enter the val for item number- " + str(i + 1) + "- "))
    List.append((w,val))
w = int(input("Enter the val of w- "))
print("Maximum val for the given w val- ", KS(w, List))
