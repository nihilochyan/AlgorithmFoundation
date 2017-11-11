#recursion
m = [[0, 0, 0, 0, 0, 0] for x in range(0, 6)]
p = [30, 35, 15, 5, 10, 20, 25]

def matrixChainMulti(p, i, j):
    if i == j:
        m[i][j] = 0
        return m[i][j]
    m[i][j] = float('inf')
    for k in range(i, j):
        temp = matrixChainMulti(p, i, k) + matrixChainMulti(p, k+1, j) + p[i-1] * p[k] * p[j]
        if temp < m[i][j]:
            m[i][j] = temp
    return m[i][j]

print(matrixChainMulti(p, 0, 5))
print(m)


#dynamic
n = len(p) - 1
s = [[0 for x in range(0, n+1)] for y in range(0, n+1)]
def memoryMatrix(p):
    m = [[0 for x in range(0, n+1)] for y in range(0, n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            m[i][j] = float('inf')
    return lookChain(m, p, 1, n)

def lookChain(m, p, i, j):
    if m[i][j] < float('inf'):
        return m[i][j]
    elif i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = lookChain(m, p, i, k) + lookChain(m, p, k+1, j) + p[i-1] * p[k] * p[j]
            if(q < m[i][j]):
                m[i][j] = q
                s[i][j] = k
    return m[i][j]

def printPartition(s, i, j):
    if i == j:
         print('A'+str(i),end='')
    else:
        print('(', end='')
        printPartition(s, i, s[i][j])
        printPartition(s, s[i][j]+1, j)
        print(')', end='')

memoryMatrix(p)
print(s)
printPartition(s, 1, 6)