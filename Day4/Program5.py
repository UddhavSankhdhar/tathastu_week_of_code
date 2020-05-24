novotes = int(input("Enter number of votes- "))
votes = []
for i in range(novotes):
    votes.append(input("Enter the name of the candidate- "))
Cad = []
for name in votes:
    Cad.append((name, votes.count(name)))
Cad.sort(key=lambda x: x[0], reverse=True)
Cad.sort(key=lambda x: x[1])
print("Name of the candidate who won- ", Cad[-1][0])
