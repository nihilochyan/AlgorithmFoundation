s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def recursiveActivitySelector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:  #find the first activity in Sk to finish
        m = m + 1
    if m <= n:
        return [m,] + recursiveActivitySelector(s, f, m, n)
    else:
        return None

#iterative one
def greedyActivitySelector(s, f):
    n = s.length
    A = [1,]
    k = 1
    for m in range(2, n+1):
        if s[m] >= f[k]:
            A = A + [m,]
            k = m
        return A

