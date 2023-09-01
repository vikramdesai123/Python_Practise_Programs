def heighst_pair(arr):
    l=len(arr)
    
    if l<2:
        print("no pair exist")
        return
    
    x=arr[0];y=arr[1]
    for i in range(l):
        for j in range(i+1,l):
            if arr[i]*arr[j]>x*y:
                x=arr[i];y=arr[j]
    return x,y

arr=[1,2,3,0,21,2,4,5]
print(heighst_pair(arr))