def sort(arr, size):
    j = 0
    for i in range(size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1  
    return j

def PositiveNoSearch(arr, size):
    for i in range(size):
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    for i in range(size):
        if (arr[i] > 0):
            return i + 1
    return size + 1


def missingSearch(arr, size):
    shift = sort(arr, size)
    return PositiveNoSearch(arr[shift:], size - shift)

arr = [5,10,12,2,1,-1]
arr_size = len(arr)
smallestNo = missingSearch(arr, arr_size)
print("The smallest positive missing number- ", smallestNo)


