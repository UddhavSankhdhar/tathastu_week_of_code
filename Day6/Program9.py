def Smallest(arr, n, k):
    arr.sort()
    return arr[k - 1]


if __name__ == '__main__':
    arr = [2,7,14,9,8]
    n = len(arr)
    k = 2
    print("Smallest K'th element- ",
          Smallest(arr, n, k))
