p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

#recursion
def cutRod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        temp = p[i] + cutRod(p, n - i)
        if q < temp:
            q = temp
    return q

print('four divide by one#recursion', cutRod(p, 4))

#Dynamic
def extendedBottomUpCutRod(p, n):
    r = [0 for x in range(0, n+1)]
    s = [0 for x in range(0, n+1)]
    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1, j+1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r[n]

print('four divide by one#dynamic', extendedBottomUpCutRod(p, 4))
