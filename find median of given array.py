def median(arr):
    for i in range (len(arr)-1):
        small = i
        for j in range(i+1,len(arr)):
            if arr[small]>arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    if len(arr)%2 != 0:
        l = len(arr)+1
        index = (l//2)-1
        return arr[index]
    else:
        index = (len(arr)//2)-1
        return arr[index]

arr = [2,4,1,3,5,7,6,9,10]
print(median(arr))