# Given an array of integers, find the sum of its elements.

def arraySum(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum

arr = [1,2,3,4,5]
print(arraySum(arr))