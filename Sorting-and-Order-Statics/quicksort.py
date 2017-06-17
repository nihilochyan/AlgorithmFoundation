from random import choice

a = []
for i in range(0, 20):
    a.append(choice(range(0, 20)))
print(a)


def sub_sort(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array, low, high):
    if low < high:
        key_index = sub_sort(array, low, high)
        quick_sort(array, low, key_index)
        quick_sort(array, key_index+1, high)


if __name__ == "__main__":
    quick_sort(a, 0, len(a)-1)
    print(a)