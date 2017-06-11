from random import choice

a = []
for i in range(0, 20):
    a.append(choice(range(0, 20)))
print(a)


def merge(a, l, p, r):
    left = a[l: p+1]
    right = a[p+1: r+1]
    i = 0
    j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1

"""
l = lowest index
r = highest index
"""
def merge_sort(a, l, r):
    if l < r:
        p = int((l + r)/2)
        merge_sort(a, l, p)
        merge_sort(a, p+1, r)
        merge(a, l, p, r)


if __name__ == '__main__':
    merge_sort(a, 0, len(a)-1)
    print(a)
