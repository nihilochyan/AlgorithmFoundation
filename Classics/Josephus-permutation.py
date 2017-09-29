def permutationOutput(m, n): #　步长 人数
    """complexity = O(n)"""
    s = 0
    for i in range(2, n+1):
        s = (s+m)%i
    print('the winner is ',s+1)

permutationOutput(2, 80)


def josephus(n, m, k): #　分别为：人数，出圈步长，起使报数位置
    """complexity = O(m) 有问题"""
    if m == 1:
        k = [n, k + n - 1][k == 1]
    else:
        for i in range(1, n+1):
            if k + m < i:
                x = (i - k + 1) / (m - 1) - 1
                if i + x < n:
                    i = i + x
                    k = k + m * x
                else:
                    k = k + m * (n - i)
                    i = n
            k = (k + m - 1) % i + 1
    print(k)

josephus(80, 2, 78)