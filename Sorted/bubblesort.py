from random import choice

a = []
for i in range(0, 20):
    a.append(choice(range(0, 20)))
print(a)


def bubblesort(a):
    for i in range(len(a)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(a)-i-1):  # ｊ为列表下标
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

bubblesort(a)
print(a)
