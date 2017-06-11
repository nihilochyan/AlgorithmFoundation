import math


def findMaxCrossingSubarray(a, low, mid, high):
    left = float("-inf")
    sum = 0
    maxLeft = 0
    maxRight = 0
    for i in range(mid, low-1, -1):
        sum = sum + a[i]
        if sum > left:
            left = sum
            maxLeft = i
    right = float("-inf")
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + a[j]
        if sum > right:
             right = sum
             maxRight = j
    return [maxLeft, maxRight, left+right]


def findMaxSubarray(a, low, high):
    """
    :param a: array
    :param low: lowest index
    :param high: highest index
    :return: max subarray
    """
    if high == low:
        return (low, high, a[low])
    else:
        mid = math.floor((low+high)/2)
        [left_low, left_high, left_sum] = findMaxSubarray(a, low, mid)
        [right_low, right_high, right_sum] = findMaxSubarray(a, mid+1, high)
        [cross_low, cross_high, cross_sum] = findMaxCrossingSubarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        else:
            return [cross_low, cross_high, cross_sum]


from random import choice

a = []
for i in range(0, 20):
    a.append(choice(range(-20, 20)))
print(a)
subset = findMaxSubarray(a, 0, 19)
print(subset)
