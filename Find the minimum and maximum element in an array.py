def minMax(array):
    l=len(array)
    
    for i in range(l):
        for j in range(0,l-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

array=[23,34,23,43,54,7,56]
result=minMax(array)

print("minimum element is",result[0])
print("maximum element is",result[len(array)-1])
