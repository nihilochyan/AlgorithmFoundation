from random import choice

a = []
for i in range(0, 20):
    a.append(choice(range(0, 20)))
print(a)


def sift_down(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break

        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child

        else:
            break


def heap_sort(arr):
    first = len(arr)
    for start in range(first, -1, -1):
        sift_down(arr, start, len(arr)-1)

    for end in range(len(arr)-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)


if __name__ == "__main__":
    heap_sort(a)
    print(a)

