def sort0and1(arr, n):
    count = 0

    for i in range(0, n):
        if (arr[i] == 0):
            count = count + 1

    for i in range(0, count):
        arr[i] = 0

    for i in range(count, n):
        arr[i] = 1


def printarr(arr, n):
    print("Array after segregating- ", end="")

    for i in range(0, n):
        print(arr[i], end=" ")


arr = [0, 1, 0, 1, 1, 1]
n = len(arr)

sort0and1(arr, n)
printarr(arr, n)
