def Ar(m, n, s="% s"):
    print(s % ("Ar(% d, % d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return Ar(m - 1, 1, s)
    n2 = Ar(m, n - 1, s % ("Ar(% d, %% s)" % (m - 1)))
    return Ar(m - 1, n2, s)
print(Ar(1, 2))
