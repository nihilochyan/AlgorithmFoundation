p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

#n3
def optimalBST(p, q, n):
    e = [[0 for x in range(n+1)] for y in range(n+2)]
    w = [[0 for x in range(n+1)] for y in range(n+2)]
    root = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l -1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j] + q[j]
            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root, w

e, root, w = optimalBST(p, q, 5)
print(w)
print(e)
print(root)

#n2
def optimalBST2(p, q, n):
    e = [[0 for x in range(n+1)] for y in range(n+2)]
    w = [[0 for x in range(n+1)] for y in range(n+2)]
    root = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    for i in range(1, n+1):
        root[i][i] = i
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l -1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j] + q[j]
            print(root)
            print(i,j)
            if i == 1 or i == n or j==i:
                for r in range(i, j+1):
                    t = e[i][r-1] + e[r+1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r
            else:
                for r in range(root[i][j-1], root[i+1][j]+1):
                    t = e[i][r-1] + e[r+1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r
    return e, root, w

e, root, w = optimalBST2(p, q, 5)
print(w)
print(e)
print(root)