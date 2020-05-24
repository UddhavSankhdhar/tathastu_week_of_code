def find3Numbers(A, arr_size):
    for i in range(0, arr_size - 2):

        for j in range(i + 1, arr_size - 1):

            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] >0 and A[i] + A[j] + A[k]<1:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True


    return False


A = [0.1, 4, 0.45, 0.6, 0.3, 0.8]

arr_size = len(A)
find3Numbers(A, arr_size)
