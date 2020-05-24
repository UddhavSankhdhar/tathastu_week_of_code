s = int(input("Enter the number of words in the dictonary- "))
dict = []
for i in range(s):
    dict.append(input("Enter the word " + str(i + 1) + "- "))
s = int(input("Enter the number of letters(char) you want to add in the array- "))
arr= []
res= []
print("Enter the letters in array- ")
for i in range(s):
    arr.append(input())
for word in dict:
    if set(word).issubset(set(arr)):
        res.append(word)
print("Possible words- ")
print(", ".join(res) + ".")
