from random import choice

a = []
for i in range(0, 10):
    a.append(choice(range(0, 10)))
print(a)

"""
O(n2)
"""
def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i > -1 and a[i] < key:
            a[i + 1] = a[i]
            i = i - 1
        a[i+1] = key

insertion_sort(a)
print(a)