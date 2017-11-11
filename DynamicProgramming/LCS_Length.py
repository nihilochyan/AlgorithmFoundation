X = ['B','D','C','A','B','A']
Y = ['A','B','C','B','D','A','B']


def LGSLength(X, Y):
    m = len(X)
    n = len(Y)
    b = [['' for i in range(0, m+1)] for i in range(0, n+1)]
    c = [[0 for i in range(0, m+1)] for i in range(0, n+1)]
    for i in range(1, m+1):
        c[0][i] = 0
    for j in range(1, n+1):
        c[j][0] = 0
    for j in range(1, m+1):
        for i in range(1, n+1):
            if X[j-1] == Y[i-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '-'
    return c, b

c, b = LGSLength(X, Y)
for i in range(0, len(c)):
    print()
    for j in range(0, len(c[i])):
        print(b[i][j], end='')
    print()
    for j in range(0, len(b[i])):
        print(c[i][j], end='')
