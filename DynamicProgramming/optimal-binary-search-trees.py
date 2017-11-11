def optimalBST(p, q, n):#n3
    e = [[0 for x in range(n+1)] for y in range(n+2)]
    w = [[0 for x in range(n+1)] for y in range(n+2)]
    root = [[0 for x in range(n+1)] for y in range(n+1)]
    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j] + q[j]
            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root

